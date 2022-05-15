'''
Counter is a sub-class which is used to count hashable objects. It implicitly creates a hash table of an iterable when invoked.

'''

from collections import Counter

repeat_dict = {}

my_string = 'Abcdaabcefgheegga'
char_counts = Counter(my_string)
print(char_counts)
print(len(char_counts))
print(f'1. {list(char_counts)} \n')
print(f'2. Most common = {char_counts.most_common()} \n')
print(f'3. {dict(char_counts.items())} \n')

# create a dictionary from char_counts
print(f'4. {dict(char_counts.most_common())} \n')

# count of char 'a'
print('Char "a" counts = ', char_counts['a'])

# create a sorted dictionary from char_counts
for key, value in char_counts.items():
    repeat_dict[key] = value
print('Repeat dict = ', repeat_dict)

my_list = ['one', 'two', 'three', 'four', 'two', 'one', 'one', 'four', 'one']
word_counts = Counter(my_list)
print(word_counts.most_common())

# count of word 'two'
print(word_counts['two'])

#
print(Counter(my_list).items())

print(Counter(my_list).keys())

print(Counter(my_list).values())
