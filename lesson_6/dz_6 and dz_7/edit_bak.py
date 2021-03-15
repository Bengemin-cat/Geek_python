from sys import argv
import os

with open('bakery.csv', 'r', encoding='utf-8') as rf:
    with open('new_bakery.csv', 'w', encoding='utf-8') as wf:
        for idx, line in enumerate(rf, start=1):
            if idx == int(argv[1]):
                wf.write(f'{" ".join(argv[2:])} \n')
                continue
            wf.write(line)
os.remove('bakery.csv')
os.rename('new_bakery.csv', 'bakery.csv')
