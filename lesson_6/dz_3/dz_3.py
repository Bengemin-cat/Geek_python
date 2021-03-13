import json
import itertools

with open('users.csv', encoding='utf-8') as users:
    with open('hobby.csv', encoding='utf-8') as hobby:
        hob_use = itertools.zip_longest(users, hobby)
        dict_hob_use = {}
        for i in hob_use:
            dict_hob_use.setdefault(str(i[0]).strip().replace(',', ' '), str(i[1]).strip())

with open('result.json', 'w', encoding='utf-8') as result:
    if 'None' in dict_hob_use:
        exit(1)
    else:
        json.dump(dict_hob_use, result, indent=5, ensure_ascii=False)