with open('nginx_logs.txt') as log:
    gen = (line.split() for line in log)
    list_gen = [(i[0], i[5].replace('"', ''), i[6]) for i in gen]


f = {}
for i in range(len(list_gen)):
    if list_gen[i][0] not in f:
        f[list_gen[i][0]] = 1
    else:
        f[list_gen[i][0]] += 1

for key, value in f.items():
    if max(f.values()) == value:
        print(f'Это IP спамера  {key} и количество отправленных запросов = {value}')
        break
