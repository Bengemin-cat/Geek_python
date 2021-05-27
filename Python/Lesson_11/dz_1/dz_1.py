import re


class Data:
    __re_valid_date = re.compile(r'^\d{2}-\d{2}-\d{4}')

    def __init__(self, data):
        self.data = data

    @classmethod
    def give_namber(cls, date):
        if Data.__re_valid_date.match(date):
            return tuple(int(_) for _ in date.split('-'))
        else:
            return f'{date} введена не правильно : формат DD-MM-YYYY'

    @staticmethod
    def valid_date(obj):
        month_30 = [4, 6, 9, 11]
        if Data.__re_valid_date.match(obj):
            d, m, y = obj.split('-')
            if int(m) > 12:
                return 'Месяц указан не верно: больше 12'
            if int(d) > 31:
                return 'День указан не верно: больше 31'
            elif int(m) == 2 and int(d) > 28:
                return f'В феврале нет {d} дня'
            elif int(m) in month_30 and int(d) > 30:
                return f'В {m} месяце нет {d} дня'
            else:
                return f'{obj} - дата правильная'
        else:
            return f'Дата {obj} введена не правильно : формат DD-MM-YYYY'


print(Data.valid_date('29-р-2021'))
print(Data.give_namber('02-04-2021'))
one = Data('02-04-2021')
print(one.valid_date(one.data))
