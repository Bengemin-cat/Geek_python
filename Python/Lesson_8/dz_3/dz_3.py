from functools import wraps


def type_logger(func):
    @wraps(func)
    def logger(*args, **kwargs):
        t = func(*args, **kwargs)
        print(func.__name__, (*args, type(t)))
        return t

    return logger


@type_logger
def calc_cube(x):
    return x ** 3


calc_cube(3)
print(calc_cube.__name__)
help(calc_cube)
