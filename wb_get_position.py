import requests

def parser(art: int, query: str):
    page = 1
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Origin': 'https://www.wildberries.ru',
        'Referer': 'https://www.wildberries.ru/catalog/0/search.aspx?search=%D1%84%D1%83%D1%82%D0%B1%D0%BE%D0%BB%D0%BA%D0%B0',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    params = {
        'TestGroup': 'no_test',
        'TestID': 'no_test',
        'appType': '1',
        'curr': 'rub',
        'dest': '-1257786',
        'query': query,
        'page': str(page),
        'resultset': 'catalog',
        'sort': 'popular',
        'spp': '29',
        'suppressSpellcheck': 'false',
    }

    def parse(params, headers):
        try:
            response = requests.get('https://search.wb.ru/exactmatch/ru/common/v4/search', params=params, headers=headers)
        except:
            return 'error'
        response = response.json()
        if not response:
            return 'end' 
        count = 0
        for id_art in response['data']['products']:
            if id_art['id'] == art:
                return (count, page)
            count += 1
        return None
    
    while True:
        params['page'] = page
        res = parse(params, headers)
        if res  == 'error':
            return 'Сервис не работает.'
        elif res == 'end':
            return 'Парсинг закончен. Ничего не найдено.'
        elif res is None:
            page += 1
        else:
            return f'Скрипт нашел товар по запросу "{query}" с артикулом {art} на {res[0]} позиции, на {res[1]} странице'


art = int(input('Введите артикул: '))
print(art)
query = input('Введите запрос: ')
print(parser(art, query))
