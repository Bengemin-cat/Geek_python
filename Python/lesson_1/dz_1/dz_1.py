# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
#       до минуты: <s> сек;
#       до часа: <m> мин <s> сек;
#       до суток: <h> час <m> мин <s> сек;
#     * в остальных случаях: <d> дн <h> час <m> мин <s> сек.


eve = [' дн ', ' час ', ' мин ', ' сек ']
duration = [53, 153, 4153, 400153]
for item in duration:
    print(f'\nduration = {item}')
    tim = [item // 86400, (item % 86400) // 3600, ((item % 86400) % 3600) // 60, (((item % 86400) % 3600) % 60)]
    for i, list_eve in enumerate(eve, start=1):
        if tim[i - 1]:
            print(tim[i - 1], end=list_eve)
print()
