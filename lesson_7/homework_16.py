#
# Написать функцию, которая представит человека по переданным параметрам.
# Входные данные: Два аргумента строка(str) и положительное число(int)
# Функция должна вернуть строку.
# say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old"
# say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old"


def say_hi(name: str, years: int) -> str :
    '''
    Функция представляет человека по полученным данным.
    '''
    return f"Hi. My name is {name} and I'm {years} years old"

print(say_hi('Alex', 25))