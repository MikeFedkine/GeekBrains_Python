"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

a_string = input("Введите число a: ")
a = int(a_string)

b_string = input("Введите число b: ")
b = int(b_string)


def Division(number_1, number_2):
    if number_2 == 0:
        number_2 = int(input("Деление на 0 невозможно, попробуйте ввести другое число b: "))
        Division(number_1, number_2)
    else:
        print("Результат деления чисел", number_1/number_2)

Division(a, b)