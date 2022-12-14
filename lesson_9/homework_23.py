#
# На вход функции передаются 2 аргумента. Текст и массив слов, популярность которых необходимо определить.
# При решении этой задачи обратите внимание на следующие моменты:
#     Слова необходимо искать во всеx регистрах. Т.е. если необходимо найти слово "one", значит для него будут подходить слова "one", "One", "oNe", "ONE" и.т.д.
#     Искомые слова всегда указаны в нижнем регистре
#     Если слово не найдено ни разу, то его необходимо вернуть в словаре со значением 0 (ноль)
# Входные параметры: Текст и массив искомых слов.
# Выходные параметры: Словарь, в котором ключами являются искомые слова и значениями то, сколько раз они встречаются в исходном тексте.
# Пример:
# popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }
# Предусловия:
# Исходный текст будет состоять из букв английского алфавита в верхнем и нижнем регистре, а также пробелов.

def popular_words(my_str, my_list):
    my_str = my_str.lower().split()

    my_dict = {}

    for word in my_list:
        my_dict.setdefault(word, my_str.count(word))

    return my_dict


print(popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']))
