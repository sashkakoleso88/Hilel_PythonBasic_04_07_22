#
# Вам необходимо написать функцию, которая будет принимать список из чисел и находить среди них уникальное число.
# Пример:
# find_unique_value([1, 2, 1, 1]) -> 2
# find_unique_value([2, 3, 3, 3]) -> 2
# find_unique_value([5, 5, 5, 0.5]) -> 0.5


def find_unique_value(my_list: list):
    '''
    Функция принимает список из чисел и возвращает уникальное число.
    '''
    for i in my_list:
        if my_list.count(i) == 1:
            return i


print(find_unique_value([1, 2, 1, 1]))
print(find_unique_value([2, 3, 3, 3]))
print(find_unique_value([5, 5, 5, 0.5]))