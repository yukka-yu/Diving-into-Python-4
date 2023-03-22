# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.


def function(my_list:int, i1:int, i2:int) -> int:
    if i2 < i1:
        i1, i2 = i2, i1
    if i1 < 0:
        i1 = 0
    if i2 >= len(my_list):
        i2 = len(my_list) - 1
    return sum(my_list[i] for i in range(i1, i2 + 1))


print(function([1, 2, 3, 4, 5, 6], 2, 3))