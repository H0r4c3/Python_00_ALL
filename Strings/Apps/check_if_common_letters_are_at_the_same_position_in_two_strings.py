
def common_letters(string1, string2):
    my_zip = zip(string1, string2)
    
    #letters = [item[0] for item in my_zip if item[0] == item[1]]
    letters = [letter1 for letter1, letter2 in my_zip if letter1==letter2]
    
    return letters

string1 = 'ABCD'
string2 = 'AZCX'

result = common_letters(string1, string2)
print(result)