digit = int(input('Dведите число :  '))
s = 0
for i in range(0, digit):
    digits = int(input('Введите числo : '))
    if digits % 3 == 0:
        s += digits
print('Сумма всех чисел, которые делятся на 3 : ', s)

