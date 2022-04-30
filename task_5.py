"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
"""

my_list = [7, 5, 3, 3, 2]

print(f"Имеющийся рейтинг - {my_list}")

the_number = input("Введите число (Завершить ввод - выход): ")

while the_number != "Завершить ввод":
    for el in range(len(my_list)):
        if my_list[el] == int(the_number):
            my_list.insert(el + 1, int(the_number))
            break
        elif my_list[0] < int(the_number):
            my_list.insert(0, int(the_number))
        elif my_list[-1] > int(the_number):
            my_list.append(int(the_number))
        elif my_list[el] > int(the_number) and my_list[el + 1] < int(the_number):
            my_list.insert(el + 1, int(the_number))
    print(f"получившийся рейтинг - {my_list}")
    the_number = input("Введите число (Завершить ввод - выход): ")


