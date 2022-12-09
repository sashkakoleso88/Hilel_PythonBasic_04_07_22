#
# Ваша задача написать функцию, которая прочитает заданный файл, очистит текст от html-тэгов, и запишет этот текст в другой файл.
# html-тэг всегда начинается с "<" и заканчивается на ">" Т.е. нужно удалить эти символы и все, что между ними.
# Функция получает на вход два параметра - имя файла, который нужно очистить, и имя файла, куда нужно записать очищенный текст. Имя файла, куда нужно писать, можно задать значением по умолчанию.
# Пример файлов во вложении - файл который нужно очистить (расширение html) и файл, с очищенным текстом.
# Доп. задача для тех, кто захочет усложнить решение - попробуйте убрать строки, в которых нет информации.

file_html = r'C:\Users\sashka_koleso\Downloads\draft.html'
file_txt = r'test_writting.txt'

def copy_file(html, txt):
    with open(html, 'r', encoding='UTF-8') as opened_file_html:
        with open(txt, 'w', encoding='UTF-8') as opened_file_txt:

            list_of_strings = opened_file_html.readlines()
            x = ''.join(list_of_strings)

            open_tag = '<'
            end_tag = '>'
            tag = x[x.find(open_tag) : x.find(end_tag) + 1]

            while tag in x:
                x = x.replace(tag,'')
                tag = x[x.find(open_tag): x.find(end_tag) + 1]
                if tag == '':
                    break

            opened_file_txt.write(x)


copy_file(file_html, file_txt)
