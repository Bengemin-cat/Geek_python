# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
# Check
# № 1
list_price = [572.8, 46.51, 97, 748.58, 2.45, 99.09, 478, 68, 23.48, 60, 9.5]
list_max_5 = []
while len(list_max_5) < 5:
    list_max_5.insert(0, list_price.pop(list_price.index(max(list_price))))
print(list_max_5)
# № 2
list_price.sort()
print(list_price[-5:])
