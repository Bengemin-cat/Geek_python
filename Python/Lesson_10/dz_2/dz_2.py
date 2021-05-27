from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def calculation(self):
        pass


class Coat(Clothes):

    def __init__(self, v):
        self.v = v

    @property
    def calculation(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def calculation(self):
        return 2 * self.h + 0.3


print(f'{Coat(58).calculation:.2f} это пальто')
print(f'{Suit(185).calculation} это костюм')
print(f'Общий расход ткани {Coat(58).calculation + Suit(185).calculation:.2f}')
