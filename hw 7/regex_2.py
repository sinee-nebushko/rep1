from re import fullmatch

p=['bar', 'car', 'far', 'war', '0ar', '$ar']
n = ['bag', 'for', 'star', 'care']

for x in p + n:
    match = fullmatch('(\w|[$])ar', x)
    if match:
        print(x, match, match.group(0), match.group(1))
    else:
        print(x, None)