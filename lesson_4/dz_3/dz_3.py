import requests
from datetime import date
from decimal import Decimal
from xml.etree import ElementTree


def currency_rates(currency):
    resp = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').content
    use_root = ElementTree.fromstring(resp)
    today = use_root.attrib['Date'].split('.')
    for element in use_root:
        if currency.upper() == element.find('CharCode').text:
            name = element.find('Name').text
            coin = element.find('Value').text
            coin = Decimal(coin.replace(',', '.'))
            print(f'Курс {name} = {coin} рубля')
            print(date(int(today[-1]), int(today[-2]), int(today[0])))
            break


currency_rates(input('Введите код валюты, Например USD, EUR: '))
