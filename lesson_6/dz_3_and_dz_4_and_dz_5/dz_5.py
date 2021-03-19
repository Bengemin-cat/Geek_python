import sys
import itertools


def argv_user(name_1, name_2, name_3):
    with open(name_1, encoding='utf-8') as users:
        with open(name_2, encoding='utf-8') as hobby:
            with open(name_3, 'w', encoding='utf-8') as users_hobby:
                hob_use = itertools.zip_longest(users, hobby)
                for i in hob_use:
                    users_hobby.writelines(f'{str(i[0]).strip().replace(",", " ")} : {str(i[1]).strip()}\n')


file = sys.argv
argv_user(file[1], file[2], file[3])
