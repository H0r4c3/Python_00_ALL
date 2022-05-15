''

roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

roman_list = ['L', 'X', 'X', 'V', 'I']

# get the values from roman dictionary having the keys in roman_list
latin_list = [roman[key] for key in roman_list]
print(latin_list)