'https://automatetheboringstuff.com/chapter5/'
'https://automatetheboringstuff.com/files/'

'''
The program loops over each character in the message variable’s string, counting how often each character appears. 
The setdefault() method call ensures that the key is in the count dictionary (with a default value of 0) so the program doesn’t throw a KeyError error 
when count[character] = count[character] + 1 is executed.
'''

# If you import the pprint module into your programs, you’ll have access to the pprint() and pformat() functions that will “pretty print” a dictionary’s values. 
# This is helpful when you want a cleaner display of the items in a dictionary than what print() provides. 
import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)

p_string = pprint.pformat(count)
print(p_string)