class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return f'{self.cell}'

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        return self.cell - other.cell if self.cell - other.cell > 0 else f'Разность двух клеток меньше нуля'

    def __mul__(self, other):
        return self.cell * other.cell

    def __floordiv__(self, other):
        return Cell(self.cell // other.cell)

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.cell // rows)]) + '\n' + '*' * (self.cell % rows)


cell_1 = Cell(5)
cell_2 = Cell(6)
cell_3 = Cell(18)
print(cell_1 + cell_2)
print(cell_1 - cell_3)
print(cell_3 - cell_2)
print(cell_3 // cell_2)
print(cell_2.make_order(3))
