import calendar
a = input('Введите вашу дату рождения в формате(день.месяц.год): ')
data = a.split('.')
d = calendar.weekday(int(data[2]), int(data[1]), int(data[0]))
weekdays = ['Понедельник','Вторник','Среда','Четверг','Пятница','Суббота','Воскресенье']
print( weekdays[d])
