def open_list():
    with open('nginx_logs.txt', 'r', encoding='utf-8') as log:
        gen = (line.split() for line in log)
        return [(i[0], i[5].replace('"', ''), i[6]) for i in gen]


if __name__ == '__main__':
    print(open_list())
