#
# Ваша задача — написать программу, которая перемножает все цифры,
# введенного пользователем целого числа, пока оно не станет меньше либо равной 9.
# Число вводит пользователь с клавиатуры, и оно всегда должно быть больше нуля.
# Примеры:
# 999 -> 2 # 999 -> 9 * 9 * 9 = 729 -> 7 * 2 * 9 = 126 -> 1 * 2 * 6 = 12 -> 1 * 2 = 2
# 1000 -> 0
# 423 -> 8
# 1 -> 1


users_num = int(input())
#users_num = 999
#users_num = 1000
#users_num = 423
#users_num = 1

x = 1

if users_num <= 9:
    print(users_num)
else:
    while users_num :
        last_digit = users_num % 10
        x *= last_digit
        users_num //= 10

        if users_num == 0:
            if x <= 9:
                print(x)
                break
            else:
                users_num = x
                x = 1