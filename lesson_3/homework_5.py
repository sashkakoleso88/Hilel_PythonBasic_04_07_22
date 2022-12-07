#Ваша программа должна разделить один список на два и поместить их в новый список. Т.е. в итоге должен получиться список из 2-х списков.
#Если в начальном списке нечетное количество элементов, то в первом списке должно быть больше элементов.
#Если в списке нет элементов, то должн быть создан список с двумя пустыми списками.
#Примеры: Было - стало
#[1, 2, 3, 4, 5, 6] => [[1, 2, 3], [4, 5, 6]]
#[1, 2, 3] => [[1, 2], [3]]
#[1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
#[1] => [[1], []]
#[] => [[], []]


my_list = [1, 2, 3, 4, 5, 6]
#my_list = [1, 2, 3]
#my_list = [1, 2, 3, 4, 5]
#my_list = [1]
#my_list = []


len_of_list = len(my_list)

if len_of_list == 0:
    my_list = [[], []]
    print(my_list)
elif len_of_list == 1:
    my_list = [my_list, []]
    print(my_list)
elif len_of_list % 2 == 0:
    my_list = [my_list[: int(len_of_list / 2)], my_list[int(len_of_list / 2):]]
    print(my_list)
elif len_of_list % 2 != 0:
    my_list = [my_list[: int(len_of_list/2) + 1], my_list[int(len_of_list / 2) + 1:]]
    print(my_list)


