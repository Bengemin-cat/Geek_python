# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):
from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


# Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?

def get_jokes(namber=min(len(nouns), len(adverbs), len(adjectives)), flag=False):
    """

    :param namber: Колличество сгенерированых шуток
    :param flag: Если True  то сгенерирует не больше минимального колличества значений в списках
    :return: Возвращает список  шуток
    """
    if flag and namber > min(len(nouns), len(adverbs), len(adjectives)):
        return f'Число уникальных шуток превышено максимум: {min(len(nouns), len(adverbs), len(adjectives))}'
    list_d = []
    new_nouns, new_adverbs, new_adjectives = nouns, adverbs, adjectives.copy()
    while namber > 0:
        ch_new_nouns, ch_new_adverbs, ch_new_adjectives = choice(new_nouns), choice(new_adverbs), choice(
            new_adjectives)
        if not flag:
            list_d.append(f'{ch_new_nouns} {ch_new_adverbs} {ch_new_adjectives}')
        elif flag:
            list_d.append(f'{ch_new_nouns} {ch_new_adverbs} {ch_new_adjectives}')
            new_nouns.remove(ch_new_nouns)
            new_adverbs.remove(ch_new_adverbs)
            new_adjectives.remove(ch_new_adjectives)
        namber -= 1

    return list_d


print(get_jokes(8))
