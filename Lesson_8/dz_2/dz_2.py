import re

RE_LOG = re.compile(r'([\d\.]+)[\s-]+\[([\d\w\/:\s+]*)\]\s\"(\w*)\s([\/\w]+)\s(?:[\w\d\/\."]*)\s(\d+)\s(\d*)',
                    re.IGNORECASE)


with open(r'C:\Users\vlad\Desktop\Python\Vladimir_Vyalkov\Geek_Python\lesson_6\dz_1 and dz_2\nginx_logs.txt',
          encoding='utf-8') as logs:
    for line in logs:
        print(*map(lambda x: x.group(1, 2, 3, 4, 5, 6), RE_LOG.finditer(line)), sep=',')
