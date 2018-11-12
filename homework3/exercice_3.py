import json

with open("text.txt", 'rb') as text_1:
    s = text_1.read(4)
    if s == b'\x8b\xad\xf0\x0d':
        rest = bytearray(text_1.read()[4:].decode())
        for i in rest:
            rest_desh = 255 - rest[i]
            text_1.write(bytearray(rest_desh))
    elif s == b'\xca\xfe\xba\xbe':
        rest_desh = bytearray(text_1.read()[4:].decode())
        text_1.write(rest_desh)
text_1.close()

with open("text.txt", 'wb') as t:
    name = input('Введите ваше имя:  ')
    age = input('Введите ваш возраст:  ')
    profession = input('Введите вашу профессию:  ')

    a = dict()
    a['age'] = age
    a['profession'] = profession
    j = dict()
    j[name] = a
    tex = json.dumps(j)
t.close()

with open("text.txt", 'rb') as text_2:
    read_text = text_2.read()
    z = input('Вы хотите зашифровать информацию? да/нет')
    b = bytearray(read_text)
    n = 'CAFEBABY'
    n_1 = n.encode()
    m = '8BADFOOD'
    m_1 = m.encode()
    header_1 = bytearray(n_1)
    header_2 = bytearray(m_1)
    if z == 'да':
        header = header_1
    else:
        header = header_2

text_2.write(header)
text_2.write(b)
text_2.close()
