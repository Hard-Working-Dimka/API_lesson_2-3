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
    response.raise_for_status()
    decoded_response = response.json()

    if decoded_response.get('error'):
        raise requests.exceptions.HTTPError
    return decoded_response['response']['short_url']


def count_clicks(vk_token, short_link):
    disassembled_url = urlparse(short_link)
    payload = {
        "v": "5.199",
        'key': disassembled_url.path[1],
        'access_token': vk_token,
        'interval': 'forever',
    }
    url = 'https://api.vk.ru/method/utils.getLinkStats'

    response = requests.post(url, data=payload)
    response.raise_for_status()
    decoded_response = response.json()

    if decoded_response.get('error'):
        raise requests.exceptions.HTTPError
    if not decoded_response['response']['stats']:
        return 0
    return decoded_response['response']['stats'][0]['views']


def is_shorten_link(url):
    disassembled_url = urlparse(url)
    return disassembled_url.netloc == 'vk.cc'


def main():
    load_dotenv()
    vk_token = os.environ['VK_TOKEN']

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
