import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
import os
import argparse


def is_bitlink(bitlink, token):
    api_url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    response = requests.get(api_url, headers=headers)
    return response.ok


def count_clicks(bitlink, token):
    api_url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    response = requests.get(api_url, headers=headers)
    response.raise_for_status()  
    return response.json().get('total_clicks', 0)


def shorten_link(long_url, token):
    api_url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    request_data = {
        'long_url': long_url,
    }
    response = requests.post(api_url, headers=headers, json=request_data)
    response.raise_for_status()  
    return response.json().get('link')


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='Shorten or get click count for a Bitly link'
        )
    parser.add_argument(
        'url', type=str, help='The Bitly link or the URL to shorten'
        )
    args = parser.parse_args()

    load_dotenv()
    bitly_token = os.environ['BITLY_TOKEN']
    url = args.url  
    try:
        if is_bitlink(url, bitly_token):
            click_count = count_clicks(urlparse(url).path, bitly_token)
            print(f"Количество кликов по ссылке: {click_count}")
        else:
            shortened_url = shorten_link(url, bitly_token)
            print("Сокращенная ссылка:", shortened_url)
    except FileNotFoundError as e:
        print(f"Файл не найден: {e}")
    except ValueError as e:
        print(f"Ошибка значения: {e}")
    except requests.RequestException as e:
        print(f"Ошибка запроса: {e}")
    except KeyError as e:
        print(f"SOME_KEY: {e}")
        
