from re import fullmatch

p=['hog', 'rack', 'shock', 'pocked']
n = ['rock', 'core', 'roar', 'doors', 'looolz']

for x in p + n:
    match = fullmatch('(r|c|d|l)o(ck|re|ar|ors|oolz)', x)
    if match:
        print(x, match, match.group(0), match.group(1))
    else:
        print(x, None)