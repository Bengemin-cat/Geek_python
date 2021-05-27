src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

new_src = []

for el in src:
    if el not in new_src:
        new_src.append(el)
    else:
        new_src.remove(el)
print(new_src)


