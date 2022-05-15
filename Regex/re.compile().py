
import re

s = 'sfsfs13-10-2021dfsfsad05-12-2021fsad'
r = re.compile('[0-9]{2}-[0-9]{2}-[0-9]{4}')
result = r.findall(s)
print(result)


s = 'oga_kuuapa_fe_'
r = re.compile('[a-z]*_')
my_list = r.findall(s)
print(my_list)


s = 'abcdefghijklmnopqrstuvwxyz'
r = re.compile('[aeiou]+')
vowels = r.findall(s)
print(vowels)

