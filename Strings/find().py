'https://www.programiz.com/python-programming/methods/string/find'

'''
The find() method returns the index of first occurrence of the substring (if found). If not found, it returns -1.

Syntax of String find()
The syntax of the find() method is:

str.find(sub[, start[, end]] )

find() Parameters
The find() method takes maximum of three parameters:

sub - It is the substring to be searched in the str string.
start and end (optional) - The range str[start:end] within which substring is searched.
'''

message = 'Python is a fun programming language'

# check the index of 'fun'
print(message.find('fun'))

# Output: 12


quote = 'Do small things with great love'

# Substring is searched in 'things with great love'
print(quote.find('small things', 10))

# Output: -1