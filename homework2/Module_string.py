import string
with open(r"C:\Users\Виктория\PycharmProject\rep1\text.txt", 'rt') as t:
    text = t.read()

wordlist = text.split()
words = []
for i in range(len(wordlist)):
    word = wordlist[i]
    character = word.strip(string.punctuation)
    if character.isalpha():
        words.append(character)
ch = ''.join(words).lower()

print(text)
print('В данном тексте ', len(words), ' слов')
print(len(ch),' - общее количество букв')

char_list = []
for k in range(0, len(ch)):
    char = ch[k]
    j = int(k)
    m = 0
    if char not in char_list:
        for j in range(j, len(ch)):
            if char == ch[j]:
                m = m + 1
                char_list.append(char)
        print(char, m)

text_lines = text.splitlines()
d = int(len(text_lines)//2)

part_1 = text_lines[:d:]  # второе двоеточие необязательно, просто text_lines[:d]
part_2 = text_lines[d:]

rewr_text = part_2+part_1
rewr_text = '\n'.join(rewr_text)

tw = open(r"C:\Users\Виктория\PycharmProject\rep1\text.txt", 'w')
tw.write(rewr_text)

tw.close()
t.close()

