import random
a = random.randint(1, 10)
print(a)
b = int(input('Компьютер загадал число от 1 до 10.\n Ваш вариант : '))
while a!=b:
    b = int(input('продолжай '))
    continue
print('Ура! Правильный ответ - ', b)

