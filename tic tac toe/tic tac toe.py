field = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

for k in range(1, 10):
    if k % 2 == 0:
        print('Ходят нолики')
        m = '0'
    else:
        print('Ходят крестики')
        m = 'X'
    v = 0

#Я паталась вынести всё это нидестоящее добро в модуль, но(!) вопреки всему, функции не видели переменные даже если они были помечены как global
    # так потому что их нужно было передавать аргументами функции :)
    # т.е. не def make_turn(), а def make_turn(field, x, y)
    # global указывает, что переменная является глобальной для _модуля_,
    # поэтому если функция и переменные находятся в разных модулях,
    # их действительно не будет видно даже с global

    def print_field():x
        print('+---+---+---+')
        print('| %s |' % ' | '.join(field[0]))
        print('+---+---+---+')
        print('| %s |' % ' | '.join(field[1]))
        print('+---+---+---+')
        print('| %s |' % ' | '.join(field[2]))
        print('+---+---+---+')

x = int(input('Введите строку:  '))  # Просим координаты для Х
y = int(input('Введите столбец:  '))

    def make_turn():


    def check_range(x, y):
        if x < 1 or x > 3 or y < 1 or y > 3 or field[x - 1][y - 1] != ' ':
            print('Данная ячейка занята или не существует.')  # Всякое бывает. Предупреждаем.
            x = int(input('Введите другую строку:  '))  # Просим другие координаты для Х
            y = int(input('Введите друрой столбец:  '))
            field[x - 1][y - 1] = m
        else:
            field[x - 1][y - 1] = m


    def check_rows():
        global v
        for n in field:
            if n[0] == n[1] == n[2] != ' ':  # Проверяем все строки
                print('Победил - ', n[0])
                v += 1
                break


    def check_cols():
        global v
        for o in range(0, 2):  # проверяем все столбцы
            if field[0][o] == field[1][o] == field[2][o] != ' ':
                print('Победил - ', field[0][o])
                v += 1
                break


    def check_diagonals():
        global v
        if field[0][0] == field[1][1] == field[2][2] != ' ':
            print('Победил - ', field[1][1])
            v += 1
        elif field[0][2] == field[1][1] == field[2][0] != ' ':
            print('Победил - ', field[1][1])
            v += 1


    print_field()
    make_turn()
    check_range()
    check_rows()
    check_cols()
    check_diagonals()
    print_field()
    if v == 0 and k == 9:
        print('Ничья')
        break
    elif v == 1:
        break
