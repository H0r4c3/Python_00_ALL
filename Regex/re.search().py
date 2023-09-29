'https://www.guru99.com/python-regular-expressions-complete-tutorial.html'

'''
re.search(): Finding Pattern in Text
re.search() function will search the regular expression pattern and return the first occurrence. 
Unlike Python re.match(), it will check all lines of the input string. 
The Python re.search() function returns a match object when the pattern is found and “null” if the pattern is not found

In order to use search() function, you need to import Python re module first and then execute the code. 
The Python re.search() function takes the “pattern” and “text” to scan from our main string
'''
import re

# 1. Example
print('\n1. Example:\n')

patterns = ['software testing', 'guru99']
text = 'software testing is fun?'
for pattern in patterns:
    print('Looking for "%s" in "%s" ->' % (pattern, text), end=' ')
    if re.search(pattern, text):
        print('found a match!')
else:
    print('no match')
    
    
# 2. Example
print('\n2. Example:\n')

s = 'sfsfs13-10-2021dfsfsad05-12-2021fsad'
pattern = '[0-9]{2}-[0-9]{2}-[0-9]{4}'
m = re.search(pattern, s)
print(f'm = {m}')
print(f'm.group() = {m.group()}')
print(f'm.span() = {m.span()}')


# 3. Example
print('\n3. Example:\n')

s = "1name.txt"
pattern = '[^1234567890].+'
regex = re.compile(pattern)

result = regex.search(s)
print(result)


# 4. Example
print('\n4. Example:\n')
s = 'Horace123Horace456Horace'
regex1 = 'Horace$'
regex2 = 'Horace'
result1 = re.search(regex1, s)
result2 = re.match(regex2, s)
print(result1)
print(result2)


# 5. Example
print('\n5. Example:\n')
s = 'abcdefghijkl'
patterns_list = ['ghijkl', 'ijkl', 'jkl']

for regex in patterns_list:
    result = re.search(regex + '$', s)
    print(result)
