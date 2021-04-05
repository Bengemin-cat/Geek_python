class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    dividend, divider = input('>> ').split('/')
    if int(divider) == 0:
        raise OwnError('Деление на  ноль')
except (ValueError, OwnError) as err:
    print(err)
else:
    print(int(dividend) / int(divider))
