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
        'interval': 'forever',
    }
    url = 'https://api.vk.ru/method/utils.getLinkStats'

    response = requests.post(url, data=payload)
    if response.json().get('error'):
        raise requests.exceptions.HTTPError
    if not response.json()['response']['stats']:
        return 0
    return response.json()['response']['stats'][0]['views']


def is_shorten_link(url):
    parsed = urlparse(url)
    return parsed.netloc == 'vk.cc'


def main():
    load_dotenv()
    vk_token = os.getenv('VK_TOKEN')

    url = input('Введите ссылку, которую хотите сократить: ')

    try:
        if is_shorten_link(url):
            print('Число переходов по ссылке: ', count_clicks(vk_token, url))
        else:
            print('Короткая ссылка: ', shorten_link(vk_token, url))
    except requests.exceptions.HTTPError:
        print('Неправильная ссылка!')


if __name__ == '__main__':
    main()
