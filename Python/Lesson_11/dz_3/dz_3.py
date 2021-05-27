class NumberError(Exception):
    def __init__(self, txt):
        self.text = txt


number_list = []
while True:
    number = input('Введите число: ')
    if number == 'stop':
        break
    try:
        if number.isalpha():
            raise NumberError('Не число')
        else:
            if '.' in number:
                number_list.append(float(number))
            else:
                number_list.append(int(number))

    except NumberError as err:
        print(err)

print(number_list)
