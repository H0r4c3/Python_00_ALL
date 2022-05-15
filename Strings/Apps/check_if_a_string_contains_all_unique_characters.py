'https://www.geeksforgeeks.org/python-program-to-check-if-a-string-contains-all-unique-characters/'

'''
Method #1: Using Built-in Python Functions:
Count the frequencies of characters using Counter() function
If the keys in frequency dictionary(gives the count of distinct characters) is equal to length of string then print True else False
'''

from collections import Counter
 
def unique_chars(string):
 
    freq = Counter(string)
    print(freq)
    print(list(freq)) # list with unique characters
 
    if(len(freq) == len(string)):
        return True
    else:
        return False
 
 
 
my_string = "abcddefag"
print(unique_chars(my_string))



'''
Method #2: Another solution is to create an array of boolean values, where the flag at the index i indicates whether character i in the alphabet is contained in the string. The second time you see this character you can immediately return false. 
You can also return false if the string length exceeds the number of unique characters in the alphabet.  
'''

def isUniqueChars(st):
 
    # String length cannot be more than
    # 256.
    if len(st) > 256:
        return False
 
    # Initialize occurrences of all characters
    char_set = [False] * 128
 
    # For every character, check if it exists
    # in char_set
    for i in range(0, len(st)):
 
        # Find ASCII value and check if it
        # exists in set.
        val = ord(st[i])
        if char_set[val]:
            return False
 
        char_set[val] = True
 
    return True
 
# driver code
st = "abcd"
print(isUniqueChars(st))