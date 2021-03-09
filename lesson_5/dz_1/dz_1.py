def odd_nums(n):
    for value in range(1, n + 1, 2):
        yield value


odd_to_15 = odd_nums(15)

for i in range(10):
    print(next(odd_to_15, 'done'))
