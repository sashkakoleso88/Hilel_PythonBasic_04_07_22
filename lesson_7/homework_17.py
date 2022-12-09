#
# На вход функции будет передано одно предложение.
# Необходимо вернуть его исправленную копию так, чтобы оно всегда начиналось с большой буквы и заканчивалось точкой.
# Обратите внимание на то, что не все исправления необходимы.
# Если предложение уже заканчивается на точку, то добавлять еще одну не нужно, это будет ошибкой
# Входные аргументы: Строка (string).
# Выходные аргументы: Строка (string).
# Пример:
# correct_sentence("greetings, friends") == "Greetings, friends."
# correct_sentence("hello") == "Hello."
# correct_sentence("Greetings, friends") == "Greetings, friends."
# correct_sentence("Greetings, friends.") == "Greetings, friends."
# correct_sentence("greetings, friends.") == "Greetings, friends."

def correct_sentence(string: str) -> str :
    correct_string = list(string)
    if not correct_string[0].isupper():
        correct_string[0] = correct_string[0].upper()

    if not correct_string[-1] == '.':
        correct_string.append('.')

    return ''.join(correct_string)


print(correct_sentence("greetings, friends"))
print(correct_sentence("hello"))
print(correct_sentence("Greetings, friends"))
print(correct_sentence("Greetings, friends."))
print(correct_sentence("greetings, friends."))