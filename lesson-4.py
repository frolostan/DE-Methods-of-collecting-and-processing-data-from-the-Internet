# Методы сбора и обработки данных из сети Интернет. GU_Data_Engineering_1542 (31.01.2022)
# Выполнил: Фролов Виктор Сергеевич

'''
Написать приложение, которое собирает основные новости с сайта на выбор news.mail.ru, lenta.ru, yandex-новости. Для парсинга использовать XPath. Структура данных должна содержать:
название источника;
наименование новости;
ссылку на новость;
дата публикации.
Сложить собранные новости в БД
Минимум один сайт, максимум - все три
'''


import requests
from lxml import html
import pymongo


client = pymongo.MongoClient('127.0.0.1', 27017)
db = client.Lenta

url = 'https://lenta.ru/parts/news/'
headers = {'UserAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
session = requests.Session()
response = session.get(url, headers=headers)

tree = html.fromstring(response.text)
news = tree.xpath('//div[@class="parts-page__wrap"]//h3/text()')
hrefs = tree.xpath('//div[@class="parts-page__wrap"]//a[@class="card-full-news _parts-news" ]/@href')
times = tree.xpath('//div[@class="parts-page__wrap"]//time/text()')

listik = []
for i in range(len(news)):
    x = {'Title: ': 'Lenta.ru',
    'Event: ':'',
    'URL: ':'',
    'Time: ':''}
    x['Event: '] = news[i]
    x['URL: '] = hrefs[i]
    x['Time: '] = times[i]
    listik.append(x)
    

print(len(news))
print(len(hrefs))
print(len(times))

db.news.insert_many(listik)
# client.drop_database('Lenta')
print(listik)





