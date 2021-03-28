class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'salary': wage, 'premium': bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'Имя Фамилия: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'{sum(self._income.values())} тенге')


worker = Position('Акакий', 'Акакович', 'хранитель шинели', 42500, 21000)

worker.get_full_name()
worker.get_total_income()
