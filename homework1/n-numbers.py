a = int(input('введите число   '))
s=0
for i in range(0,a):
    b = int(input('Введите числo  '))
    if b%3==0:
        s=s+b
print('Сумма всех чисел, которые делятся на 3 : ',s)

