'https://www.guru99.com/python-regular-expressions-complete-tutorial.html'

'''
findall() module is used to search for “all” occurrences that match a given pattern. 
In contrast, search() module will only return the first occurrence that matches the specified pattern. 
findall() will iterate over all the lines of the file and will return all non-overlapping matches of pattern in a single step.

For example, here we have a list of e-mail addresses, and we want all the e-mail addresses to be fetched out from the list, 
we use the method re.findall() in Python. It will find all the e-mail addresses from the list.


'abc'                 # Matches the literal 'abc'
r'\w+'                # Matches a word
r'\d+\s\w+'           # Matches '1555 dogs'
r'\d+-\d+-\d+\s.+'    # Matches '2005-12-05 Jons birthday'
r'\s+'                # Matches any number of whitespace

'abc(def)ghi'         # Matches the literal 'abcdefghi' and captures 'def' as capture group #1
r'abc\(def\)ghi'      # Matches the literal 'abc(def)ghi'
'''


import re

abc = 'guru99@google.com, careerguru99@hotmail.com, users@yahoomail.com'
emails = re.findall(r'[\w\.-]+@[\w\.-]+', abc)
for email in emails:
    print(email)
    
    
my_string = '123 abc456def 789xyz 13 xxx 321'
#only digits as word (between spaces)
r1 = re.compile('\s\d+\s')
print(r1.findall(my_string))
#print(re.findall(r1, my_string))

# only digits
r2 = re.compile('\d+')
print(r2.findall(my_string))
#print(re.findall(r2, my_string))

# starts with digits or digits not between chars or ends with digits
r3 = re.compile('^\d+|[^\w]\d+[^\w]|\d+$')
print(r3.findall(my_string))
#print(re.findall(r3, my_string))



my_string = '%^3One @5two7# 22three#%# #@5334# fo##%%^r'
all_words = re.findall(r"[0-9a-zA-Z-']+", my_string)
print(all_words)

all_numbers = re.findall(r"[0-9]+", my_string)
print(all_numbers)


# find all five characters long word in a string
text = 'The quick brown fox jumps over the lazy dog.'
print(re.findall(r"\b\w{5}\b", text))