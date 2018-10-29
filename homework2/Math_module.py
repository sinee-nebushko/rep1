import math

# обращай внимание на предупреждения PEP8

sp = []
k = 0
while k < 3:
    st = int(input('Введите сторону треугодьника  '))
    sp.append(st)
    k += 1

a = sp[0]
b = sp[1]
c = sp[2]
if a + b > c and b + c > a and a + c > b:
    cos1 = (a * a + b * b - c * c) / (2 * a * b)
    cos2 = (a * a + c * c - b * b) / (2 * a * c)
    cos3 = (b * b + c * c - a * a) / (2 * b * c)

    ugol_1 = math.degrees(math.acos(cos1))
    ugol_2 = math.degrees(math.acos(cos2))
    ugol_3 = math.degrees(math.acos(cos3))
    print(ugol_1, ugol_2, ugol_3)
else:
    print('Треугольник с данными сторонами не существует.')
