# Методы сбора и обработки данных из сети Интернет. GU_Data_Engineering_1542 (31.01.2022)
# Выполнил: Фролов Виктор Сергеевич


'''
1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев 
для конкретного пользователя, сохранить JSON-вывод в файле *.json.

'''



from github import Github
import requests
import json


user = 'frlm4ster'
url = 'https://api.github.com/users/{}'.format(user)
data = requests.get(f"https://api.github.com/users/{user}")
json_data = data.json()
print(json_data)

with open('data.json', 'w') as f:
    json.dump(json_data, f)

'''
2. Изучить список открытых API (https://www.programmableweb.com/category/all/apis). 
Найти среди них любое, требующее авторизацию (любого типа). 
Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.
Если нет желания заморачиваться с поиском, возьмите API вконтакте (https://vk.com/dev/first_guide). 
Сделайте запрос, чтобы получить список всех сообществ на которые вы подписаны.

'''


import vk_api


session = vk_api.VkApi(token='vk1.a.1aYQ7w3DBJ5OGS_c7djX3_mRjVaCoDegNRzIV_pt-TSZhR4KsYwjEW4reNGBEPQfxGm1LfrZjMLdKCvp1GFFPahmmGt3TCW5Xfkd3zQHximNMt0TBTNUZ6gVnaHFmUfvdel-icJ3z9dk5PTAtBrcsG2DFu0Dtma5lc-rjA4IaYjvxn8jdiHAGAvn3zXJs1O2')
vk = session.get_api()




def get_groups(user_id):
    groups = session.method("groups.get", {"user_id": user_id } )
    print(groups)


get_groups(511581258)


