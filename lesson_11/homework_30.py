#
# Задача усложняется. Ваша функция, как и раньше, должна возвращать True если число четное, и False если число нечетное, но при этом НЕЛЬЗЯ использовать деление и функции связанные с ним. Т.е. запрещено использовать /, //, % и divmod
# Сложность ещё заключается и в том, чтобы найти решение, которое бы не зависело от размера числа :)
# Входные данные: Целое число.
# Выходные данные: Логический тип.
# Пример:
# is_even(2494563894038**2) == True
# is_even(1056897**2) == False
# is_even(24945638940387**3) == False


def is_even(num):
    return num in range(0, num +1, 2)


print(is_even(2494563894038**2)) #True
print(is_even(1056897**2)) #False
print(is_even(24945638940387**3)) #False
print(is_even(3)) #False
print(is_even(2)) #True
print(is_even(11)) #False
print(is_even(23472938742984729837424728904729423428342384902384092384502834528548258235328520983847293479283429874978)) #True