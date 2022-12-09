#
# Пользователь вводит строку. Ваша задача - проверить, может ли эта строка, быть именем переменной.
# Переменная не может начинаться с цифры, состоять только из цифр, не может содержать заглавные буквы
# и знаки пунктуации, кроме нижнего подчеркивания "_" .
# Также, она не может быть ни одним из зарегистрированных слов.
# При этом имя переменной, может состоять только из одного нижнего подчеркивания "_" .
# Зарегистрированные слова можно взять из keyword.kwlist.
# В итоге проверки, на печать выводится True, если такое имя переменной допустимо, и False - в противном случае.
# Примеры имен переменных и результат (=> на печать выводить не нужно :))
# _ => True
# x => True
# get_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False


from string import ascii_lowercase , digits
from keyword import kwlist
valid_chars = ascii_lowercase + digits + '_'

users_var = '_'
#users_var = 'x'
#users_var = 'get_value'
#users_var = 'Get_value'
#users_var = 'get_Value'
#users_var = 'getValue'
#users_var = '3m'

flag = True

if users_var in kwlist:
    flag = False
elif users_var.isdigit():
    flag = False
elif not users_var.islower():
    flag = False
else:
    if users_var[0].isdigit():
        flag = False
    else:
        for char in users_var:
            if char not in valid_chars:
                flag = False
                break
if users_var == '_':
    flag = True

print(flag)

