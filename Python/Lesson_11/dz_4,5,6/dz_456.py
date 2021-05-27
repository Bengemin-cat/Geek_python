import pprint

class Stock:
    def __init__(self):
        self.stock = {
            'Printer': {'Canon': {'LaserJet1020': {'price': 15000, 'count': 15, 'color': 'цветной'},
                                  'LaserJet1010': {'price': 18000, 'count': 5, 'color': 'цветной'}
                                  }
                        },
            'Scanner': {},
            'Xerox': {}

        }

    def give_equipment(self, type_, product):
        if type_ in self.stock:
            if product.brand in self.stock[type_]:
                if product.model in self.stock[type_][product.brand]:
                    self.stock[type_][product.brand][product.model]['count'] += product.count
                else:
                    self.stock[type_][product.brand].setdefault(
                        product.model, {'price': product.price, 'count': product.count, 'color': product.color})


class Equipment:
    def __init__(self, brand, model, price, count):
        self.brand = brand
        self.model = model
        self.price = price
        self.count = count


class Printer(Equipment):

    def __init__(self, brand, model, price, count, color):
        super().__init__(brand, model, price, count)
        self.color = color


class Scanner(Equipment):
    def __init__(self, brand, model, price, count, resolution):
        super().__init__(brand, model, price, count)
        self.resolution = resolution


class Xerox(Equipment):
    def __init__(self, brand, model, price, count, speed_copy):
        super().__init__(brand, model, price, count)
        self.speed_copy = speed_copy


storage = Stock()

f = Printer('Canon', 'LaserJet2120', 15000, 0, 'цветной')
storage.give_equipment('Printer', f)
pprint.pprint(storage.stock)

# while True:
#     print(
#         'Выберите соответствующую цифру для выполнения операции  \n1: Добавить товар\n2: Переместить товар \n3: Выйти')
#     mode = int(input('Введите значение: '))
#     if mode == 3:
#         print('Склад закрыт')
#         break
#     elif mode == 1:
#         print('\rКакой товар хотите добавить\n1: Printer\n2: Scanner\n3: Xerox')
#         mode = int(input('Введите значение: '))
#         if mode == 1:
#             printer_brand = input("Выберите Бренд:\n"
#                                   "1: HP\n"
#                                   "2: Samsung\n"
#                                   "3: Canon\n>> "
#                                   )
#             model = input('Введите модель без пробелов:\n>> ')
#             price = input('Введите цену:\n>> ')
#             count = input('Введите количество:\n>> ')
#             printer_color = input('Введите скорость подачи:\n>> ')
