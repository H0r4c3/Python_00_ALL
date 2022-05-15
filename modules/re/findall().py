'''
'abc'                 # Matches the literal 'abc'
r'\w+'                # Matches a word
r'\d+\s\w+'           # Matches '1555 dogs'
r'\d+-\d+-\d+\s.+'    # Matches '2005-12-05 Jons birthday'
r'\s+'                # Matches any number of whitespace

'abc(def)ghi'         # Matches the literal 'abcdefghi' and captures 'def' as capture group #1
r'abc\(def\)ghi'      # Matches the literal 'abc(def)ghi'
'''

import re

my_string = '%^3One @5two7# 22three#%# #@5334# fo##%%^r'
all_words = re.findall(r"[0-9a-zA-Z-']+", my_string)
print(all_words)

all_numbers = re.findall(r"[0-9]+", my_string)
print(all_numbers)


# find all five characters long word in a string
text = 'The quick brown fox jumps over the lazy dog.'
print(re.findall(r"\b\w{5}\b", text))