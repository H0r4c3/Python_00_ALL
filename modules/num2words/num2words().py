'https://pypi.org/project/num2words/'

'''
num2words is a library that converts numbers like 42 to words like forty-two. 
It supports multiple languages (see the list below for full list of languages) and 
can even generate ordinal numbers like forty-second (although this last feature is a bit buggy for some languages at the moment).
'''

from num2words import num2words
def checkio(number):
    result = num2words(number)
    result = result.replace('-', ' ').replace('and', '').replace('  ', ' ')
    print(result)
    
    return result


assert checkio(4) == 'four', "1st example"
assert checkio(133) == 'one hundred thirty three', "2nd example"
assert checkio(12) == 'twelve', "3rd example"
assert checkio(101) == 'one hundred one', "4th example"
assert checkio(212) == 'two hundred twelve', "5th example"
assert checkio(40) == 'forty', "6th example"
assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
print('Done!')

# for romanian language
print(num2words(123, lang='ro'))