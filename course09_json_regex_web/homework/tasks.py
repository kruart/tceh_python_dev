# Реализовать две функции: write_to_file(data) и read_file_data().
# Которые соотвественно: пишут данные в файл и читают данные из файла.
import json
import re
from pprint import pprint

import requests


def write_to_file(data):
    with open('file.txt', mode="w") as file:
        file.write(data)


def read_file_data():
    with open('file.txt') as file:
        content = file.read()
        print(content)


write_to_file('Hello, PythonWorld!!!')
read_file_data()

# Реализовать следующую логику: получать при помощи requests данные сервиса https://jsonplaceholder.typicode.com/
# (сущность можно выбрать любую, например https://jsonplaceholder.typicode.com/comments),
# выводить в консоль все пары заголовки, сохранять полученный json в файл на диск
def get_commmnets():
    response = requests.get('https://jsonplaceholder.typicode.com/comments')
    print(response.headers)
    print(response.json())

    with open('comments.json', mode='w') as file:
        file.write(json.dumps(response.json(), sort_keys=True, indent=4))


get_commmnets()


# Обратиться с странице https://habrahabr.ru/. Получить текст страницы.
# При помощи регулярных выражений нужно получить все ссылки со страницы на другие.
# Ответить себе на вопрос удобно ли так делать?
def find_all_urls(url):
    content = requests.get(url).content
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(content))
    pprint(urls)


find_all_urls('http://habrahabr.ru/')