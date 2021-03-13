import itertools

with open('users.csv', encoding='utf-8') as users:
    with open('hobby.csv', encoding='utf-8') as hobby:
        with open('users_hobby.txt', 'a', encoding='utf-8') as users_hobby:
            hob_use = itertools.zip_longest(users, hobby)
            for i in hob_use:
                users_hobby.writelines(f'{str(i[0]).strip().replace(",", " ")} : {str(next(hobby, None).strip())} \n')

