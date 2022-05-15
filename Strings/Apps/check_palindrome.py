
# 1. Method

def is_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
        
#a = str(input("Enter string:"))
a = 'abcdcba'

if(is_palindrome(a)==True):
    print("String is a palindrome!")
else:
    print("String isn't a palindrome!")


# 2. Method

import re

def valid_palindrome(s):
    s = re.sub('[^0-9a-zA-Z]', '', s.lower())
    if s[::-1] == s:
        return True
    else:
        return False
    
s = 'A man, a plan, a canal: Panama'
print(valid_palindrome(s))