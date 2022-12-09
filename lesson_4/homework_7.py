#
# Написать программу, которая перемещает все нули в конец списка.
# Ваша задача — изменить список так, что бы нули оказались в конце списка.
# Порядок ненулевых чисел должен сохранится.
# Пример:
# [0, 1, 0, 3, 12] -> [1, 3, 12, 0, 0]
# [0] -> [0]
# [1, 0, 3, 0, 0, 0, 5] -> [1, 3, 5, 0, 0, 0, 0]
# [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] -> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]



example = [0, 1, 0, 3, 12]
#example = [0]
#example = [1, 0, 3, 0, 0, 0, 5]
#example = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]


zeroes_list = []
answer_list = []

for element in example:
    if element == 0:
        zeroes_list.append(element)
    else:
        answer_list.append(element)

answer_list.extend(zeroes_list)
print(answer_list)