WEIGHT = 25


class Road:
    def __init__(self, width, length):
        self._width = width
        self._length = length

    def calculate_coverage(self, depth=5):
        print(
            f'{self._width} м*{self._length} м*{WEIGHT} кг*{depth} см = '
            f'{self._width * self._length * WEIGHT * depth // 1000} т.')
        return


street = Road(20, 5000)

street.calculate_coverage(5)
