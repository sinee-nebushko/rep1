a = input('Введите строку 1  ')
b = input('Введите строку 2  ')

# не совсем то, что нужно было
# ты проверяешь, что слова из второй строки встречаются в первой,
# а нужно было проверить, что вторая строка является подстрокой первой, например:
# 'abcd', 'ab' -> True ('abcd' = 'ab' + 'cd')
#                                 ^^
# 'abcd', 'cd' -> True ('abcd' = 'ab' + 'cd')
#                                        ^^
# 'abcd', 'bc' -> True ('abcd' = 'a' + 'bc' + 'd')
#                                       ^^
# 'abcd', 'ef' -> False ('ef' нигде не встречается в строке 'abcd')
# 'abcd', 'ac' -> False ('ac' нигде не встречается в строке 'abcd', хоть и встречаются символы a и c)
line_1 = a.split(' ')
line_2 = b.split(' ')
for i in line_1:
    for j in line_2:
        if i == j:
            break

print('Часть строки "', a, '" входит в строку "', b, '"')


