import sys


def argv_user(name_1, name_2, name_3):
    with open(name_1, encoding='utf-8') as users:
        with open(name_2, encoding='utf-8') as hobby:
            with open(name_3, 'w', encoding='utf-8') as users_hobby:
                for user in users:
                    line = f'{user.strip()} : {str(next(hobby, None).strip())}'
                    users_hobby.writelines(line + '\n')


_, file_1, file_2, file_3 = sys.argv
argv_user(file_1, file_2, file_3)
