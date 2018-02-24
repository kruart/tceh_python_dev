from pprint import pprint
import requests


def get_habrahabr():
    response = requests.get('http://habrahabr.ru/')
    print(response.status_code)
    print(response.headers)
    print(response.content)


def find_pet_by_tag(status):
    params = {'status': status}
    headers = {
        'Accept': 'application/json'
        # 'Accept': 'application/xml'
    }
    url = 'http://petstore.swagger.io/v2/pet/findByStatus'

    response = requests.get(url, params=params, headers=headers)
    print(response.status_code)
    print(response.headers)
    pprint(response.content)


if __name__ == '__main__':
    # get_habrahabr()

    find_pet_by_tag('string')