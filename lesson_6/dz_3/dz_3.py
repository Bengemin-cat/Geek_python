import json

with open('users.csv', encoding='utf-8') as users:
    with open('hobby.csv', encoding='utf-8') as hobby:
        dict_hob_use = {user.strip().replace(',', ' '): str(next(hobby, None)).strip() for user in users}

with open('result.json', 'w', encoding='utf-8') as result:
    json.dump(dict_hob_use, result, indent=5, ensure_ascii=False)
