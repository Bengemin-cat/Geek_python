from itertools import zip_longest


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        st = ''
        for i in self.matrix:
            st += f"{''.join(str(i)).strip('[]').replace(',', '')}\n"
        return st

    def __add__(self, other):
        # s = []
        # for i, j in zip_longest(self.matrix, other.matrix,fillvalue=[]):
        #     f = []
        #     for cel_1, cel_2 in zip_longest(i, j, fillvalue=0):
        #         f.append(cel_1 + cel_2)
        #     s.append(f)
        # return Matrix(s)
        return Matrix([[cel_1 + cel_2 for cel_1, cel_2 in zip_longest(i, j, fillvalue=0)]
                       for i, j in zip_longest(self.matrix, other.matrix, fillvalue=[])])


matrix = Matrix([[31, 22], [37, 43], [51, 86, 5]])
matrix_2 = Matrix([[3, 5], [2, 4], [-1, 64]])
matrix_3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
matrix_sum_2_3 = matrix_2 + matrix_3
print(matrix_sum_2_3)
print(matrix + matrix_sum_2_3)
