"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

new_f = open('test.txt', 'w')
new_line = input('Введите текст \n')
while new_line:
    new_f.writelines(new_line)
    new_line = input('Введите текст \n')
    if not new_line:
        break

new_f.close()
new_f = open('test.txt', 'r')
content = new_f.readlines()
print(content)
new_f.close()

