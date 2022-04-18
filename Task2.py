"""
2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""

time = input("Введите время в секундах: ")
time_new = int(time)

hours = time_new // 360
minutes = (time_new-hours*360) // 60
seconds = time_new - hours*360 - minutes*60


print("Переведенное время: ", hours, ":", minutes, ":", seconds)