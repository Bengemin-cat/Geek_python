class Stock:
    def __init__(self):
        self.stock = {
            'Printer': {},
            'Scanner': {},
            'Xerox': {}
        }

    def give_equipment(self, type_, product):
        if product.model in self.stock[type_]:
            self.stock[type_][product.model] += 1
        else:
            self.stock[type_][product.model] = 1


class Equipment:
    def __init__(self, model, price, description):
        self.model = model
        self.price = price
        self.description = description

    def show_model(self):
        return self.model

    def show_price(self):
        return self.price

    def show_type_(self):
        return self.description


class Printer(Equipment):

    def __init__(self, model, price, description, color):
        super().__init__(model, price, description)
        self.color = color


class Scanner(Equipment):
    def __init__(self, model, price, description, resolution):
        super().__init__(model, price, description)
        self.resolution = resolution


class Xerox(Equipment):
    def __init__(self, model, price, description, speed_copy):
        super().__init__(model, price, description)
        self.speed_copy = speed_copy


storage = Stock()
p = Printer('HP', 1500, 'Printer', 'color')
s = Scanner('Canon', 18400, 'Scanner', '1600x900')
x = Xerox('Samsung', 42900, 'Xerox', '20')

storage.give_equipment(p.description, p)
print(storage.stock)
print('=' * 80, )
storage.give_equipment(s.description, s)
print(storage.stock)
print('=' * 80)
storage.give_equipment(x.description, x)
print(storage.stock)
print('=' * 80)
