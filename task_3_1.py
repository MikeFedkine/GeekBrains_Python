"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
"""

winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

print("Введите месяц")
month = input()

if int(month) in winter:
    print("Время года: Зима")
elif int(month) in spring:
    print("Время года: Весна")
elif int(month) in summer:
    print("Время года: Лето")
elif int(month) in autumn:
    print("Время года: Осень")
else:
    print("Такого месяца нет в году")


