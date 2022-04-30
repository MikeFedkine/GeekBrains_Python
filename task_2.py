"""
2. Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

print("Введите количество планируемых элементов в списке: ")
count = input()
task_2_list = []
i = 0
while i < int(count):
    task_2_list.append("")
    print ("Введите", i+1, " ", "Элемент")
    task_2_list[i] = input()
    i = i + 1

print("Полученный список ", task_2_list)

m = 0
if int(count) % 2 == 0:
    print("Четное количество элементов")
    while m < int(count):
        a = task_2_list[m]
        b = task_2_list[m+1]
        task_2_list[m] = b
        task_2_list[m+1] = a
        m = m + 2
else:
    print("Нечетное количество элементов")
    while m < int(count)-1:
        a = task_2_list[m]
        b = task_2_list[m+1]
        task_2_list[m] = b
        task_2_list[m+1] = a
        m = m + 2


print("Измененный список ", task_2_list)

