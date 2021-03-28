class Road:
    weight = 25

    def __init__(self, l, w):
        self._length = l
        self._width = w

    def street_asphalt(self, thickness=5):
        return print(f'{self._length * self._width * self.weight * thickness // 1000} тонн')


street = Road(20, 5000)

street.street_asphalt(6)
