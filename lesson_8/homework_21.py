#
# Ваша задача — написать функцию, которая будет проверять, является ли предложение палиндромом.
# Палиндромом — предложение, которое читается одинаков слева на право и справа налево.
# Функция принимает на вход строку, а возвращает булевое значение True\False
# Пример:
# is_palindrome('A man, a plan, a canal: Panama') -> True
# is_palindrome('0P') -> False
# is_palindrome('a.') -> True


def is_palindrome(my_str):

    clean_str = ''

    for i in my_str.lower():
        if i.isalpha() or i.isdigit():
            clean_str += i

    return clean_str == clean_str[::-1]


print(is_palindrome('A man, a plan, a canal: Panama'))
print(is_palindrome('0P'))
print(is_palindrome('a.'))