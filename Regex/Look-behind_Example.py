'https://betterprogramming.pub/demystifying-look-ahead-and-look-behind-in-regex-4a604f99fb8c'

'''
look-behind is used when the pattern appears before a desired match. 
You’re “looking behind” to see if a certain string of text has the desired pattern behind it. If it does, then that string of text is a match.
'''


# Positive look-behind

'''
In a positive look-behind, you want to find an expression A that has the expression B (i.e., the pattern) before it. 
Its syntax is (?<=B)A .
'''

import re

text = "With great power comes great responsibility."
pattern = r'(?<=great )\b\w+\b'
matches = re.findall(pattern, text)
print(matches)




# Negative Look-behind

'''
Finally, in negative look-behind, you are interested in finding an expression A that does not have the expression B (i.e., the pattern) before it. 
Its syntax is: (?<!B)A . It is the opposite of a positive look-behind.
'''

'''
Now, let’s say you want to find any complete word which does not have the pattern "great " before it in our example text string. 
This time, as you walk from the start to the end of the string, you are “looking behind” for words that do not have "great " before them.
'''

text = "With great power comes great responsibility."
pattern = r'(?<!great )\b\w+\b'
matches = re.findall(pattern, text)
print(matches)