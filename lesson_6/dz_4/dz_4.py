with open('users.csv', encoding='utf-8') as users:
    with open('hobby.csv', encoding='utf-8') as hobby:
        with open('users_hobby.txt', 'w', encoding='utf-8') as users_hobby:
            for user in users:
                line = f'{user.strip()} : {str(next(hobby, None).strip())}'
                users_hobby.writelines(line + '\n')
