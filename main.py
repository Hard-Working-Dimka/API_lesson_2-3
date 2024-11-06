import os

import requests
from dotenv import load_dotenv
from urllib.parse import urlparse


def shorten_link(vk_token, url):
    payload = {
        "v": "5.199",
        'url': url,
        'access_token': vk_token,
    }
    url = 'https://api.vk.ru/method/utils.getShortLink'

    response = requests.post(url, data=payload)
    if response.json().get('error'):
        raise requests.exceptions.HTTPError
    return response.json()['response']['short_url']


def count_clicks(vk_token, short_link):
    parsed = urlparse(short_link)
    payload = {
        "v": "5.199",
        'key': parsed.path[1],
        'access_token': vk_token,
        'interval': 'forever'
    }
    url = 'https://api.vk.ru/method/utils.getLinkStats'

    response = requests.post(url, data=payload)
    if response.json().get('error'):
        raise requests.exceptions.HTTPError
    return response.json()['response']['stats'][0]['views']


def main():
    load_dotenv()
    vk_token = os.getenv('VK_TOKEN')

    url = input('Введите ссылку, которую хотите сократить: ')

    try:
        short_link = shorten_link(vk_token, url)
        print('Сокращенная ссылка: ', short_link)

        clicks_count = count_clicks(vk_token, short_link)
        print('Число переходов по ссылке: ', clicks_count)
    except requests.exceptions.HTTPError:
        print('Неправильная ссылка ')


if __name__ == '__main__':
    main()
