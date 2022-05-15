'How to split a string at every nth character in Python'
'https://www.kite.com/python/answers/how-to-split-a-string-at-every-nth-character-in-python'


my_string = "abcde"

split_strings = []
n  = 2 # the number of characters where the string will be split

for index in range(0, len(my_string), n):
    split_strings.append(my_string[index : index + n])

print(split_strings)