from dz_1 import open_list


list_gen = open_list()
f = {}
for i in range(len(list_gen)):
    if list_gen[i][0] not in f:
        f[list_gen[i][0]] = 1
    else:
        f[list_gen[i][0]] += 1


max_value = max(f.values())
for key, value in f.items():
    if max_value == value:
        print(f'Это IP спамера  {key} и количество отправленных запросов = {value}')

