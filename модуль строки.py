import string
t = open(r"C:\Users\Виктория\PycharmProject\rep1\text.txt",'rt')
text = t.read()

sp_slov = text.split()
slova = []
for i in range (len(sp_slov)):
    sl = sp_slov[i]
    sl = sl.strip(string.punctuation )
    if sl.isalpha():
        slova.append(sl)
b = ''.join(slova).lower()

print(text)
print('В данном тексте ',len(slova),' слов')
print(len(b),' - общее количество букв')

l=[]
for k in range(0, len(b)):
    buk = b[k]
    j = int(k)
    m = 0
    if buk not in l:
        for j in range(j, len(b)):
            if buk == b[j]:
                m = m + 1
                l.append(buk)
        print(buk, m)

te= text.splitlines()
d= int(len(te)//2)

pol_1 =  te[:d:]
pol_2 = te[d:]

itog = pol_2+pol_1
itog='\n'.join(itog)

tw = open(r"C:\Users\Виктория\PycharmProject\rep1\text1.txt",'a')
tw.write(itog)

tw.close()
t.close()

