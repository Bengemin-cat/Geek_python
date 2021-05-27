class ComplexNumb:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexNumb(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumb(self.a * other.a - (self.b * other.b), self.b * other.a)

    def __str__(self):
        return f'{self.a} + {self.b} * i'


one = ComplexNumb(1, 8)
two = ComplexNumb(3, 4)
print(one*two)
