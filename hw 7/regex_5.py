from re import sub

str = '''Now you can watch the video again and test your listening skills without the text.
      Reading is a very important language learning skill. 
      It helps you improve all parts of the English language – vocabulary, spelling, grammar, and writing.'''

a = sub('\sa\s', ' ', str)
a = sub('\san\s', ' ', a)
a = sub('\sthe\s',' ', a)

print(a)