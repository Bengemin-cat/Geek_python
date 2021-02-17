# Реализовать склонение слова «процент» для чисел до 20.
# Например, задаем число 5 — получаем «5 процентов», задаем число 2 — получаем «2 процента».
# Вывести все склонения для проверки.


for x in range(20):
    edit = 'процент'
    if x % 10 == 1 and x % 100 != 11:
        print(x, edit)
    elif 2 <= x % 10 <= 4 and (x % 100 < 12 or x % 100 > 14):
        print(f'{x} {edit}а')

    else:
        print(f'{x} {edit}ов')
