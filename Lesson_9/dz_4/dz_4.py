class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} Понеслась')

    def stop(self):
        pass
    def turn(self, direction):
        pass

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    pass


class SportCar(Car):
    pass


class WorkCar:
    pass


class PoliceCar:
    pass
