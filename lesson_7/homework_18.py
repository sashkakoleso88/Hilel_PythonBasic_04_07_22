#
# Даны 2 строки. Необходимо найти индекс второго вхождения искомой строки в строке для поиска.
# Разберем самый первый пример, когда необходимо найти второе вхождение "s" в слове "sims".
# Если бы нам надо было найти ее первое вхождение, то тут все просто:
# с помощью функции index или find мы можем узнать, что "s" – это самый первый символ в слове "sims",
# а значит индекс первого вхождения равен 0. Но нам необходимо найти вторую "s", а она 4-ая по счету.
# Значит индекс второго вхождения (и ответ на вопрос) равен 3.
# Строка, которую нужно найти, может состоять из нескольких символов.
# Input: Две строки (String).
# Output: Int or None
# Примеры:
# second_index("sims", "s") => 3
# second_index("find the river", "e") => 12
# second_index("hi", "h") => None


def second_index(string: str, char: str) -> int :
    first_index = string.find(char)
    find_second_index = string.find(char, first_index+1)

    return find_second_index if find_second_index != -1 else None

print(second_index('sims', 's'))
print(second_index("find the river", "e"))
print(second_index("hi", "h"))