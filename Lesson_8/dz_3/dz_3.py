def type_loger(func):
    def loger(*args, **kwargs):
        t = func(*args, **kwargs)
        print(func.__name__, (*args, type(t)))
        return t

    return loger


@type_loger
def calc_cube(x):
    return x ** 3


calc_cube(3)
