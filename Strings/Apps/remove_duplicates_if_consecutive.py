'https://stackoverflow.com/questions/11460855/how-to-remove-duplicates-only-if-consecutive-in-a-string'

from itertools import groupby

s = '1112233344455566666666677'

# 1. Method

my_list = [i for i, _ in groupby(s)]
print(my_list)

my_string = ''.join(my_list)
print(my_string)




# 2. Method

lst = list(s)

prev_value = None

for number in lst[:]: # the : means we're slicing it, making a copy in other words
    if number == prev_value:
        lst.remove(number)
    else:
        prev_value = number
        
print(lst)

my_string = ''.join(lst)
print(my_string)