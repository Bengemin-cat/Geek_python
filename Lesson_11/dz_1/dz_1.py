class Data:

    def __init__(self, date):
        self.date = date

    @classmethod
    def take_date(cls, dmy):
        return cls(dmy.split('-'))


one = Data.take_date("03-04-2021")
print(one.date)
