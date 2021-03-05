import requests
from bs4 import BeautifulSoup


def currency_rates(currency):
    resp = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').content
    soup = BeautifulSoup(resp, 'xml')
    coin = soup.find('CharCode', text=currency).find_next_sibling('Value').string
    name_coin = soup.find('CharCode', text=currency).find_next_sibling('Name').string
    print(f'Курс {name_coin} = {coin} рублей ')


currency_rates(input('Введите Euro или Usd: ').upper())

