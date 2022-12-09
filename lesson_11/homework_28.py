#
# Напишите функцию-генератор, которая будет возвращать простые числа. Верхняя граница этого диапазона должна быть задана параметром этой функции.
# Например:
# prime_generator(10) дожна генерировать последовательность из чисел 1, 2, 3, 5, 7 . Следующее число в этой последовательности 11 и оно больше 10, поэтому оно не попадает в этот ряд


def prime_generator(num):

    count = 0
    prime_list = [1]

    for i in range(2, num+1):
        for j in range(2, i):
            if i % j == 0:
                count += 1
        if count == 0:
            prime_list.append(i)
        else:
            count = 0

    for i in prime_list:
        yield i


print(*list(prime_generator(10)))
print(*list(prime_generator(50)))
print(*list(prime_generator(100)))
print(*list(prime_generator(250)))