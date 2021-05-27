import requests
from decimal import Decimal
from xml.etree import ElementTree


def currency_rates(currency):
    resp = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').content
    use_root = ElementTree.fromstring(resp)
    for element in use_root:
        if currency.upper() == element.find('CharCode').text:
            name = element.find('Name').text
            coin = Decimal(element.find('Value').text.replace(',', '.'))
            return f'Курс {name} = {coin} рубля'


print(currency_rates('Eu'))
print(currency_rates('USd'))
print(currency_rates('Aud'))


