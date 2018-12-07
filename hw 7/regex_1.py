from re import fullmatch

p=['dog', 'log', 'lock', 'dock']
n = ['fog', 'block', 'locked']

for x in p + n:
    match = fullmatch('(l|d)o(g|ck)', x)
    if match:
        print(x, match, match.group(0), match.group(1))
    else:
        print(x, None)