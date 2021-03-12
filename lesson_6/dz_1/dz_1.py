with open('nginx_logs.txt') as log:
    gen = (line.split() for line in log)
    list_gen = [(i[0], i[5].replace('"', ''), i[6]) for i in gen]

print(list_gen)
