# Check if a string has vocals alternating with consonants

VOWELS = 'aeiouyAEIOUY'
CONSONANTS = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'
    
def check_alternates(word):
    if word[0] in VOWELS:
        if (all(char in VOWELS for char in word[0:len(word):2]) and all(char in CONSONANTS for char in word[1:len(word):2])): 
            print('1')
            return word
        else:
            print('2')
            print('NOT!')
        
    elif word[0] in CONSONANTS:
        if (all(char in CONSONANTS for char in word[0:len(word):2]) and all(char in VOWELS for char in word[1:len(word):2])):
            print('3')
            return word
        else:
            print('4')
            print('NOT!')
            
                
word = 'abecadik'
#item = '012345'
print(word[0:len(word):2])
print(word[1:len(word):2])

result = check_alternates(word)

print(result)