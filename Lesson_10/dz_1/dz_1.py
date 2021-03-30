from itertools import zip_longest
a = [[31, 22], [37, 43], [51, 86, 5]]
b = [[3, 5], [2, 4], [-1, 64]]
c = [[3, 5, 8, 3], [8, 3, 7, 1]]

class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        st = ''
        for i in self.matrix:
            st += f"|{''.join(str(i)).strip('[]').replace(',', '')}|\n"
        return st

    def __add__(self, other):
        return Matrix([[cel_1 + cel_2 for cel_1, cel_2 in zip_longest(i, j, fillvalue=0)]
                       for i, j in zip_longest(self.matrix, other.matrix, fillvalue=[])])


matrix = Matrix(a)
matrix_2 = Matrix(b)
matrix_3 = Matrix(c)
matrix_sum_2_3 = matrix_2 + matrix_3
print(matrix_sum_2_3)
print(matrix + matrix_sum_2_3)
