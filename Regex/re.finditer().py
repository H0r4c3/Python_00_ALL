'https://www.kite.com/python/docs/re.finditer'

'''
Return an iterator yielding MatchObject instances over all non-overlapping matches for the RE pattern in string. 
The string is scanned left-to-right, and matches are returned in the order found. 
Empty matches are included in the result unless they touch the beginning of another match.
'''

import re
for match in re.finditer(r"\d+", "a1b2c3"):
    print(match.span())
    
# OUTPUT
# (1, 2)
# (3, 4)
# (5, 6)



text = 'abbaaabbbbaaaaa'
pattern = 'ab'

for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found "%s" at %d:%d' % (text[s:e], s, e))
    
    
# This matches any single character (\w) and then its repetitions (\1*), if any.  
my_string = 'sdsffffse'
pattern = re.compile(r'(\w)\1*')
result_iterator = pattern.finditer(my_string)
result = [match.group() for match in result_iterator]
    
print(f'result = {result}')

