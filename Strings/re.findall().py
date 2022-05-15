'Transform a string in another string having only small letters'

import re

my_string = 'A sfsdfSS ##$BBcde'
my_new_string = ''.join(re.findall(r'[a-z]+', my_string.lower()))

print(my_new_string)
