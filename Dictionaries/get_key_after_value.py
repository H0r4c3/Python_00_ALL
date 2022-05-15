
my_dict = {'key1' : 'val1', 'key2' : 'val2', 'key3' : 'val3', 'key4' : 'val4'}

# Get the key of the value 'val3'

# Method 1
index_val = list(my_dict.values()).index('val3')
print(index_val)
my_key = list(my_dict.keys())[index_val]
print(my_key)


# Method 2
for key, value in my_dict.items():
    if value == 'val3':
        print(key)