'https://betterprogramming.pub/demystifying-look-ahead-and-look-behind-in-regex-4a604f99fb8c'

'''
Look-ahead is the type of look-around where the pattern appears ahead of the desired match. 
We are “looking ahead” to see if a certain string of text has a specific pattern ahead of it. 
If it does, then that string of text is a match.
'''

import re

# Positive look-ahead

'''
In a positive look-ahead, you want to find an expression A that has an expression B (i.e., the pattern) after it. Its syntax is A(?=B) .
'''

text = "With great power comes great responsibility."
pattern = r'\b\w+\b(?= great)'
matches = re.findall(pattern, text)
print(matches)




# Negative look-ahead

'''
A negative look-ahead, on the other hand, is when you want to find an expression A that does not have an expression B (i.e., the pattern) after it. 
Its syntax is: A(?!B) . In a way, it is the opposite of a positive look-ahead.
Now, let’s say you want to find any complete word which does not have the pattern " great" after it.
'''
text = "With great power comes great responsibility."
pattern = r'\b\w+\b(?! great)'
matches = re.findall(pattern, text)
print(matches)