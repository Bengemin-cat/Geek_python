import requests
from decimal import Decimal
from xml.etree import ElementTree


def currency_rates(currency):
    resp = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').content
    use_root = ElementTree.fromstring(resp)
    for element in use_root:
        for value in element:
            if currency.upper() == value.text:
                name = element.find('Name').text
                coin = element.find('Value').text
                coin = Decimal(coin.replace(',', '.'))
                print(f'Курс {name} = {coin}  рубля')
                break


currency_rates(input('Введите код валюты, Например USD, EUR: '))
