a = input('Введите строку 1  ')
b = input('Введите строку 2  ')
line_1 = a.split(' ')
line_2 = b.split(' ')
for i in line_1:
    for j in line_2:
        if i == j:
            break

print('Часть строки "', a, '" входит в строку "', b, '"')


