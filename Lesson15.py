# Атрибуты и методы Response
# res.url - возвращает адрес, к которому был сделан запрос
# res.status_code - возвращает код ответа
# Код ответа позволяет нам понять, всё ли хорошо или что-то произошло
# res.encoding - возвращает кодировку документа
# res.headers - возвращает заголовки
# HTTP заголовки - мета информация о документе, содержащая служебные данные. Это знакомый нам словарь,
# к отдельным элементам которого можно сразу обращаться по ключу.
# res.text - возвращает тело ответа
# res.json() или json.loads(res.text) - если тело ответа состоит из JSON, парсит его в Python объект
# res.content - возвращает тело ответа, например фото/видео

# Сессионные обьекты
import requests

requests.Session
s = requests.Session()
s.auth = ('user', 'password')
r = s.get('https://randomsite/')
print(r.status_code)

r = s.get('https://randomsite/page2')



# pip3 install requests
#import requests
# res = requests.get(url, headers=headers, params=params)

# res = requests.post(url, headers=headers, data=data)

# Передаем файл в post запросе
# url = 'https://radom/post'
# files = {'my_file': open('1.jpg', 'rb')}
# res = requests.post(url, files=files)

# delete
res = requests.delete(url, **kwargs)
# put
res = requests.put(url, data=data)

# POST: Create      PUT: Full update            PATCH: Partial update