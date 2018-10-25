a = input('Введите строку 1  ')
b = input('Введите строку 2  ')
s1 = a.split(' ')
s2 = b.split(' ')
for i in s1:
    for j in s2:
        if i == j:
            break

print('Часть строки "',a,'" входит в строку "',b,'"')


