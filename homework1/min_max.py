numb = int(input('Введите число: '))

numb_min = numb % 10
numb_max = numb % 10  #извлекаем число единиц
numb //= 10  # убираем единицы из числа

while numb > 0:
    digit = numb % 10  #извлекаем число десятков(сотен и тд.)
    if digit < numb_min:  #сравниваем единицы с десятками...
        numb_min = digit  #если число десятков меньше, заменяем единицы на него
    elif digit > numb_max:
        numb_max = digit  #если число десятков больше, заменяем единицы на него
    numb //= 10

print('Наименьшая цифра: ', numb_min)
print('Наибольшая цифра: ', numb_max)