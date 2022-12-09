#
# Ваша задача — написать программу, которая переводит число во время в читабельном виде.
# Пользователь должен ввести число больше 0 и меньше 8639999.
# Число необходимо перевести в день, часы, минуты и секунды.
# Ну и дополнительной задачей является — забота о выводе.
# Слово "день" подбирается на основе кол-ва дней, а часы, минуты и секунды должны заполняться
# нулями при одноцифровых значениях.
# Пример:
# 0 -> 0 дней, 00:00:00
# 224930 -> 2 дня, 14:28:50
# 466289 -> 5 дней, 09:31:29
# 8639999 -> 99 дней, 23:59:59
# 22493 -> 0 дней, 6:14:53
# 7948799 -> 91 день, 23:59:59


users_number = int(input())
#users_number = 0
#users_number = 224930
#users_number = 466289
#users_number = 22493
#users_number = 7948799

if not 0 <= users_number <= 8639999:
    print('Введено некорректное число, перезапустите программу и введите число от 0 до 8639999')

seconds_in_day = 86400
seconds_in_hour = 3600

days = users_number // seconds_in_day
hours = str((users_number % seconds_in_day) // seconds_in_hour).rjust(2, '0')
minutes = str(((users_number % seconds_in_day) % seconds_in_hour) // 60).rjust(2, '0')
seconds = str(users_number % 60).rjust(2, '0')

if days in range(1, 101, 20):
    days_word = 'день'
elif days in (2, 3, 4) or days in range(2, 101, 20) or days in range(3, 101, 20) or days in range(4, 101, 20):
    days_word = 'дня'
else:
    days_word = 'дней'

print(f'{days} {days_word}, {hours}:{minutes}:{seconds}')
