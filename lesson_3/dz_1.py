translate = {
    'one': 'один',
    'two': 'два',
    'tree': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    "eight": 'восемь',
    'nine': 'девять',
    'ten': 'десять'

}


def num_translate(namber):
    return translate.get(namber)


print(num_translate(input('Введите число на ангийском: ')))
