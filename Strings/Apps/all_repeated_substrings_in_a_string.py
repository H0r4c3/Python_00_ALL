import re

def repeated_substrings(my_string):
    pattern = re.findall(r'(.+)(?=.*\1)', my_string)
    
    return(pattern)

my_string = 'abc4567abc568'
result = repeated_substrings(my_string)
print(result)