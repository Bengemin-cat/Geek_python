class Stock:
    def __init__(self):
        self.stock = {}

    @classmethod
    def give_equipment(cls, obj):
        return cls(obj)


class Equipment:
    def __init__(self, model, price, description):
        self.model = model
        self.price = price
        self.description = description


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


p = Printer('HP', 1500, 'принтер', '20')
print()
