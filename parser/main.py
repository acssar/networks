import requests
from bs4 import BeautifulSoup
import fake_useragent
import csv

user = fake_useragent.UserAgent().random
headers = {
    'user-agent': user
}


def get_html(url):
    r = requests.get(url, headers=headers)
    return r


def get_content(html):
    catalog = []
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='item_info')
    for i in items:
        price = i.find('span', class_='price_value').get_text()
        price = price.replace(' ', '')
        name = i.find('span').get_text()
        if name is None:
            continue
        else:
            name = name.replace(',', ' ')
        catalog.append({
            'name': name,
            'price': price,
        })
    return catalog


def save_file(items, path):
    with open(path, 'w', encoding='utf8', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(['Названия товара', 'Цена товара'])
        for item in items:
            writer.writerow([item['name'], item['price']])


def parse():
    for URL in ['https://novosibirsk.mi-mag.ru/catalog/bytovaya_tekhnika/vertikalnye_pylesosy/', ]:
        html = get_html(URL)
        if html.status_code == 200:
            html = get_content(html.text)
        else:
            print('Error')
        filename = 'nsuparse.csv'
        save_file(html, filename)


parse()
