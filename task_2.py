"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

new_file = open('file_2.txt', 'r')
content = new_file.read()
print(f'Содержимое файла: \n {content}')
new_file = open('file_2.txt', 'r')
content = new_file.readlines()
print(f'Количество строк в файле - {len(content)}')
new_file = open('file_2.txt', 'r')
content = new_file.readlines()
for i in range(len(content)):
    print(f'Количество символов {i + 1} - ой строки {len(content[i])}')
new_file = open('file_2.txt', 'r')
content = new_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
new_file.close()