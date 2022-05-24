my_file = open('data.txt')

"""
Вывод полученного файла построчно с заменой переноса на пустой символ
"""
# for line in my_file.readlines():
#     print(line.replace('\n', ''))


for data in my_file.read(1024):
     print(data)


my_file.close()


