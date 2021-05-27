import sys

from utils import currency_rates

filename, cod = sys.argv
print(currency_rates(cod))

