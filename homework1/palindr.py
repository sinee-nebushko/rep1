a = input('Введите строку:  ')
a = ''.split(a)

# можно было сделать куда проще:
# a = a.lower()
# и получилось бы тоже самое
line = []
for i in range(len(a)):  # проверка
    ch = a[i]
    if ch.isalpha():
        ch = ch.lower()  # А вДрУг 2007 вернется
        line.append(ch)  # и сентябрь горит

a = ''.join(line)
b = a[::-1]

if a == b:
    print(' Это палиндром ')
else:
    print(' Это не палиндром ')
