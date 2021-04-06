class Stock:
    def __init__(self):
        self.stock = {
            'Printer': {
                        'HP': {

                            'price': 15000,
                            'count': 10,
                            'color': 'Цветной'

                                }
                        },
            'Scanner': {

                        },
            'Xerox': {

                    }
        }

    def give_equipment(self, type_, product):
        if product.model in self.stock[type_]:
            self.stock[type_][product.model] += 1
        else:
            self.stock[type_][product.model] = 1


class Equipment:
    def __init__(self, model, price, article):
        self.model = model
        self.price = price
        self.article = article

    def show_model(self):
        return self.model

    def show_price(self):
        return self.price

    def show_type_(self):
        return self.article


class Printer(Equipment):

    def __init__(self, model, price, article, color):
        super().__init__(model, price, article)
        self.color = color


class Scanner(Equipment):
    def __init__(self, model, price, article, resolution):
        super().__init__(model, price, article)
        self.resolution = resolution


class Xerox(Equipment):
    def __init__(self, model, price, article, speed_copy):
        super().__init__(model, price, article)
        self.speed_copy = speed_copy


storage = Stock()
while True:
    print(
        'Выберите соответствующую цифру для выполнения операции  \n1: Добавить товар\n2: Переместить товар \n3: Выйти')
    mode = int(input('Введите значение: '))
    if mode == 3:
        print('Склад закрыт')
        break
    elif mode == 1:
        print('\rКакой товар хотите добавить\n1: Printer\n2: Scanner\n3: Xerox')
        mode = int(input('Введите значение: '))
        if mode == 1:
            printer_model = input(
                "Выберите модель:\n"
                "1: HP\n"
                "2: Samsung\n"
                "3: Canon\n"
            )
            printer_price = input('Введите цену:\n>> ')
            printer_count = input('Введите артикул:\n>> ')
            printer_color = input('Введите скорость подачи:\n>> ')
