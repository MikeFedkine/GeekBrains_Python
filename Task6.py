"""
6. Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
"""


a = int(input("Введите результат первого дня в КМ "))
b = int(input("Введите цель в КМ "))
days_of_training = 1
while a < b:
        a = a * 1.1
        days_of_training += 1
        print("Результат ", days_of_training, "дня тренировок: ", a)
print(f"Нужный результат будет достигнут на %.d день тренировок" % days_of_training)