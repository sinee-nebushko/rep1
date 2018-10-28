n = int(input('Введите n: '))
numb_list = []
for dig in range(1, n):
    numb_list.append(dig)
i = 1
while numb_list[i] < n / 2:
    l = len(numb_list)
    for j in range(l - 1, i, -1):
        if numb_list[j] % numb_list[i] == 0:
            del numb_list[j]
    i += 1
numb_str = ', '.join(map(str, numb_list))

print('В промежутке от 0 до', n, ' находятся следующие простые числа: ', numb_str)
