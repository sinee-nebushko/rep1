from re import fullmatch

p=['4','5','6','87','-93','654.35']
n = ['fog', 'block', 'locked']

for x in p + n:
    match = fullmatch('(\d)|(\d+)|(-\d+)|(\d+.\d+)|(-\d+.\d+)', x)
    if match:
        print(x, match, match.group(0))
    else:
        print(x, None)