#Программа должна выполнять простые математические действия. Пользователю предлагается
#ввести числа и действие над этими числами, а программа, исходя из действия, вычисляет и печатает результат.
#Сделать проверку на то, что при делении, делитель не равен 0!


a = float(input())
b = float(input())
operation = input()

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