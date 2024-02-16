# Описание проекта

Проект "URL_BITLY" представляет собой набор функций для работы с API сервиса Bitly. С помощью этих функций пользователь может проверять битлинки, получать статистику кликов и создавать новые сокращенные ссылки.

## Требования к окружению

Python 3.x
Установленные библиотеки: requests, dotenv

### Как установить 

Склонируйте репозиторий с проектом на ваш локальный компьютер: 
(https://github.com/TimurBerdyyev/URL_BITLY.git)

Перейдите в каталог с проектом:
``` cd URL_BITLY ```

Установите необходимые библиотеки:
```pip install -r requirements.txt```


#### Примеры запуска скриптов

Запустить скрипт для работы с Bitly API:
```python link_shortener.py ```
создайте файл .env и поместите туда свой токен в переменную ```BITLY_TOKEN = "your_bitly_token_here"```

##### Примеры использования программного API
```from link_shortener import is_bitlink, count_clicks, shorten_link```

Проверка битлинга:
```bitlink = "your_bitlink_here"```
```print(is_bitlink(bitlink, BITLY_TOKEN))```

Получение стасистики кликов:
```print(count_clicks(bitlink, BITLY_TOKEN))```

Сокращение ссылки:
```long_url = "your_long_url_here"```
```print(shorten_link(long_url, BITLY_TOKEN))```






