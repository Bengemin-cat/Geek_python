import sys
from itertools import islice

with open('bakery.csv', 'r', encoding='utf-8') as baker:
    if len(sys.argv) == 1:
        for line in baker:
            print(line, end='')
    elif len(sys.argv) == 2:
        print(*(f'{i}' for i in islice(baker, int(sys.argv[1]) - 1, None)), sep='')
    elif len(sys.argv) == 3:
        print(*(f'{i}' for i in islice(baker, int(sys.argv[1]) - 1, int(sys.argv[2]) - 1)), sep='')
    else:
        print('Не правильные данные')
