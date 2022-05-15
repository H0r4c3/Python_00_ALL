

my_dict = {0: 'value0', 1 : 'value1', 2 : 'value2', 3 : 'value3'}

for key in my_dict.keys():
    print(key)
    
for value in my_dict.values():
    print(value)


# print the key in position 1
print(list(my_dict.keys())[1])

# print the 'value1' using the key named 1    
print(my_dict[1])

# print the 'value1' using the key named 1
print(my_dict.get(1))