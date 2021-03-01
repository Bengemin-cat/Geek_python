# *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():реализовать корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной

translate = {
    'zero': 'ноль',
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


def num_translate_adv(namber):
    return translate.get(namber.lower()).capitalize() if namber.istitle() else translate.get(namber.lower())


print(num_translate_adv(input('Введите число на английском: ')))
