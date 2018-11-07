import random
from functools import reduce
numb = int(input('Введите целое число:  '))
numb_list_random = []
for i in range(numb):
    numbs = random.randint(1, 9)
    numb_list_random.append(numbs)
print(numb_list_random)


def simples(x):
    sq = [x for x in numb_list_random if x in {1, 2, 3, 5, 7}]
    return sq


def evens(x):
    sq = [x for x in numb_list_random if x % 2 == 0]
    return sq


def odds(x):
    sq = [x for x in numb_list_random if x % 2 != 0]
    return sq


def slog(x, y):
    return x+y


def multitply(x,y):
    return x*y


def join(x, y):
    return str(x)+str(y)


def union(s):
    s = []
    s = set()
    return s


def reverse(x, s):
    s.insert(0, x)
    return s


def negated(x):
    return -x


def inverted(x):
    return 1/x


def squared(x):
    return x**2


func_1_filter = {'odds': odds, 'evens': evens, 'simples': simples}

func_2_reduce = {'sum': slog, 'multiply': multitply, 'join': join}

func_3_reduce = {'reverse': reverse,'union': union}

func_4_map = {'negated': negated, 'inverted': inverted, 'squared': squared}

funcname = input('Введите фунции  ')
funcs = funcname.split(' ')
a = func_1_filter.get(funcs[-1])
numb_list_random = list(filter(a, numb_list_random))
print(numb_list_random)
b = func_4_map.get(funcs[1])
numb_list_random = list(map(b, numb_list_random))
print(numb_list_random)

if funcs[0] not in func_2_reduce :
    c = func_3_reduce.get(funcs[0])
    n = str(reduce(c, numb_list_random))
    print(n)

else:
    c = func_2_reduce.get(funcs[0])
    n = str(reduce(c, numb_list_random))
    print(n)
