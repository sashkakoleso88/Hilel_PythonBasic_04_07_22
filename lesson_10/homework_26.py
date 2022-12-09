#
# Напишите функцию first_word, которая в переданной строке найдет ее первое слово.
# При решении задачи обратите внимание на следующие моменты:
# В cтроке могут встречаются точки и запятые
# Строка может начинаться с буквы или, к примеру, с пробела или точки
# В слове может быть апостроф и он является частью слова
# Весь текст может быть представлен только одним словом и все
# Входные параметры: Строка.
# Выходные параметры: Строка.
# Пример:
# first_word("Hello world") == "Hello"
# first_word("greetings, friends") == "greetings"
# first_word("don't touch it") == "don't"
# first_word("... and so on ...") == "and"
# first_word("hi") == "hi"
# first_word("Hello.World") == "Hello"

def first_word(string: str) -> str:
    '''
    Функция получает на вход строку и возвращает первое слово этой строки
    '''

    while "." in string or ',' in string:
        string = string.replace('.', ' ')
        string = string.replace(',', ' ')

    string_list = string.split()

    return string_list[0]

print(first_word("Hello world"))
print(first_word("greetings, friends"))
print(first_word("don't touch it"))
print(first_word("... and so on ..."))
print(first_word("hi"))
print(first_word("Hello.World"))