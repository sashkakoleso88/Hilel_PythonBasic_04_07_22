#
# Пользователь вводит строку, Ваша задача — преобразовать строку в hashtag.
# Парочка правил:
# никаких символов из набора string.punctuation быть не должно, в том числе и пробелов;
# итоговая длина hashtag должна быть не более 140 символов.
# Каждое слово начинается с заглавной буквы.
# Если длина хэштега более 140 символов - обрезать итоговую строку до 140 символов.
# Примеры:
# 'Python Community' -> #PythonCommunity
# 'i like python community!' -> #ILikePythonCommunity
# 'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes

from string import punctuation


example = 'Python Community'
#example = 'i like python community!'
#example = 'Should, I. subscribe? Yes!'

for char in example:
    if char in punctuation:
        example = example.replace(char, '')

example = [word.title() for word in example.split()]

example = '#' + ''.join(example)

print(example)