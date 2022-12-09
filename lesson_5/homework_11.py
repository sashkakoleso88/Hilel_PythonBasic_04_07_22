#
# Дописать калькулятор таким образом, чтобы он работал до тех пор, пока пользователь этого хочет
# Т.е. нужно делать запрос у пользователя на продолжение работы калькулятора после каждого вычисления -
#если пользователь ввел yes ( можно просто y), то новое вычисление, в противном случае - окончание работы.


next = ('yes', 'y')
answer = 'yes'
while answer in next:

    a = float(input('Введите первое число '))
    b = float(input('Введите второе число '))
    operation = input('Что будем делать ? + - / // % * ')

    if operation == '+':
        print(a + b)
    elif operation == '-':
        print(a - b)
    elif operation == '*':
        print(a * b)
    elif operation == '/':
        if b == 0:
            print('На ноль делить нельзя')
        else:
            print(a / b)
    elif operation == '//':
        if b == 0:
            print('На ноль делить нельзя')
        else:
            print(a // b)
    elif operation == '%':
        if b == 0:
            print('На ноль делить нельзя')
        else:
            print(a % b)

    answer = input('Хотите сделать ещё одно вычисление ? ')

print('Всего доброго !')