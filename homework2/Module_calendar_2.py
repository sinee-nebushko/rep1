from calendar import monthrange
weekday = input('Введите день недели, который нужно найти: ')
weekdays = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
w = weekdays.index(weekday)


def f():
    g = 2018
    m = 10
    for i in range(m, 0, -1):
        day, numb = monthrange(g, i)
        if day == w:
            return i, g

    while True:
        g -= 1
        for k in range(12, 0, -1):
            day, numb = monthrange(g, k)
            if day == w:
                return k, g


print(f())

