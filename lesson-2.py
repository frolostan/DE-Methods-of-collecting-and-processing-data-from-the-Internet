# Методы сбора и обработки данных из сети Интернет. GU_Data_Engineering_1542 (31.01.2022)
# Выполнил: Фролов Виктор Сергеевич


'''
Урок 2. Парсинг данных. HTML, DOM, XPath
Необходимо собрать информацию о вакансиях на вводимую должность 
(используем input или через аргументы получаем должность) с 
сайтов HH(обязательно) и/или Superjob(по желанию). Приложение должно 
анализировать несколько страниц сайта (также вводим через input или аргументы). 
Получившийся список должен содержать в себе минимум:
Наименование вакансии.
Предлагаемую зарплату (разносим в три поля: минимальная и максимальная и валюта. 
цифры преобразуем к цифрам).
Ссылку на саму вакансию.
Сайт, откуда собрана вакансия. (можно прописать статично hh.ru или superjob.ru)
По желанию можно добавить ещё параметры вакансии (например, работодателя и 
расположение). Структура должна быть одинаковая для вакансий с обоих сайтов. 
Общий результат можно вывести с помощью dataFrame через pandas. 
Сохраните в json либо csv.

'''


import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36'}
user_input = input('Vacancy name:')
pages_count_input = int(input('Pages count:'))
session = requests.Session()

for page in range(pages_count_input):
    url = f'https://hh.ru/search/vacancy?text={user_input}&from=suggest_post&fromSearchLine=true&area=1&page={page}&hhtmFrom=vacancy_search_list'
    response = session.get(url, headers=headers)
    dom = BeautifulSoup(response.text, 'html.parser')
    publications = dom.find_all('div', {'class':'vacancy-serp-item-body__main-info'})
    dicti = []
    
    for i in range(len(publications)):
        a_tag = publications[i].find('a')
        div_tag = publications[i].find('div', {'class':''})
        vac = a_tag.text
        href = a_tag.get('href')
        sal = div_tag.text.replace(f'{vac}', '')
        abrivvs = ['Vacancy: ','URL: ', 'Salary:', 'from: ']
        values = []
        values.append(vac)
        values.append(href)
        values.append(sal)
        values.append('HeadHunter')
        way = dict(zip(abrivvs, values))
        print(way)
        print('~~~~~~~~~~~~~~~~~~~')
        
        dicti.append(way)
print(dicti)
    
with open('data_hh.json','w') as f:
    json.dump(dicti, f)

    


        
    
    

