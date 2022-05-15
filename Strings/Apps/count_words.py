'https://www.pythonmorsels.com/exercises/9af6665915964ee7ba19fe3d762d9ca8/submit/1/'

import re
from collections import Counter

def count_words(s):
    s = s.lower()
    s1 = s.replace('!', '')
    my_list = s1.split()
    print(my_list)
    
    #rule = re.compile("don't|[a-zA-Z]+\'?s|\w")
    
    # Writing this using a rawstring (with the r prefix) is important because those \b would be interpreted as backspace characters otherwise. 
    # \b matches the empty string at the beginning or end of a word
    rule1 = re.compile(r"\b[\w'-]+\b")
    my_list2 = [''.join(re.findall(rule1, item)) for item in my_list]
    char_counts = Counter(my_list2)
    result = dict(char_counts.most_common())
    return result

s = "Don't! Oh what a day, it's a lovely day!"
result = count_words(s)
print(result)