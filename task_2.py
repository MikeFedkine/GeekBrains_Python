"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""

name = input("Введите Имя: ")
surname = input("Введите Фамилию: ")
year = input("Введите год рождения: ")
city = input("Введите город проживания: ")
email = input("Введите адрес электронной почты: ")
telephone = input("Введите контактный номер телеофна: ")

def the_result(name, surname, year, city, email, telephone):
    return " ".join([name, surname, year, city, email, telephone])

print(the_result(name, surname, year, city, email, telephone))

