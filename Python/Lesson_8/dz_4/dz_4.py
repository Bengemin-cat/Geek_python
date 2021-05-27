def val_checker(x):
    def checker(func):
        def check(args):
            if x(args):
                print(func(args))
            else:
                raise ValueError(f'Wrong namber {args}')

        return check

    return checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


calc_cube(-5)
