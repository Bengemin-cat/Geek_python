import sys

with open('bakery.csv', 'a+', encoding='utf-8') as baker:
    baker.writelines(f'{sys.argv[1]}\n')
