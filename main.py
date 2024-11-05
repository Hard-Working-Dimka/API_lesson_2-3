import os

import requests
from dotenv import load_dotenv


def shorten_link(vk_token, url):
    payload = {
        "v": "5.199",
        'url': 'https://dvmn.org/modules/',
        'access_token': vk_token,

    }
    url = 'https://api.vk.ru/method/utils.getShortLink'
    response = requests.post(url, data=payload)
    response.raise_for_status()
    d = response.json()
    print(d['response']['short_url'])


def main():
    load_dotenv()
    vk_token = os.getenv('VK_TOKEN')


if __name__ == '__main__':
    main()
