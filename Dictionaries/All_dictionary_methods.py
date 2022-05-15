'https://www.udemy.com/course/python-for-beginners-course-in-depth/learn/lecture/22664275#overview'

# 1. dict.clear() = Removes all elements of the dictionay
print('# 1.')
my_dict = {'key1' : 'val1', 'key2' : 'val2', 'key3' : 'val3', 'key4' : 'val4'}
my_dict.clear()
print(my_dict)


# 2. dict.copy() = Returns a shallow copy of a dictionary
print('# 2.')
my_dict = {'key1' : 'val1', 'key2' : 'val2', 'key3' : 'val3', 'key4' : 'val4'}
new_dict2 = my_dict.copy()
print(new_dict2)

# my_dict['key1'] = 'new_val'
# print(my_dict)
# print(new_dict2)


# 3. dict.fromkeys() = Create a new dictionary with keys from the old dictionary (or from a list), and values set to None (or set to a same "new_value")
print('# 3.')
my_dict = {'key1' : 'val1', 'key2' : 'val2', 'key3' : 'val3', 'key4' : 'val4'}
new_dict3 = dict.fromkeys(my_dict)
print(new_dict3)

keys_list = ['key11', 'key22', 'key33']
new_dict33 = dict.fromkeys(keys_list, 'new_value')
print(new_dict33)


# 4. dict.get(key, default=None) = for key, returns value or default if key does not exists
print('# 4.')
my_dict = {'key1' : 'val1', 'key2' : 'val2', 'key3' : 'val3', 'key4' : 'val4'}
print(my_dict.get('key3'))
print(my_dict.get('key100', 'Key not found!'))


# 5. dict.has_key(key) = Returns True if key in dictionary, False otherwise
print('# 5.')
print('dict.has_key() was removed from Python 3.x !!!!!!!!!!!!   Use the "in" operator instead !!!')


# 6. dict.items() = Returns a list of tuples (key, value)
print('# 6.')
my_dict = {'key1' : 'val1', 'key2' : 'val2', 'key3' : 'val3', 'key4' : 'val4'}
print(my_dict.items())
print(list(my_dict.items()))


# 7. dict.keys() = Returns a list of dictionary's keys
print('# 7.')
my_dict = {'key1' : 'val1', 'key2' : 'val2', 'key3' : 'val3', 'key4' : 'val4'}
print(my_dict.keys())
print(list(my_dict.keys()))


# 8. dict.setdefault(key, default=None) = Similar to get(), but will set dict[key] = default if key not in dictionary
print('# 8.')
my_dict = {'key1' : 'val1', 'key2' : 'val2', 'key3' : 'val3', 'key4' : 'val4'}
print(my_dict.setdefault('key3'))

my_dict.setdefault('key100', 'Key not found!')
print(my_dict)


# 9. dict.update(dict2) = adds dictionary dict2 to dict
print('# 9.')
my_dict = {'key1' : 'val1', 'key2' : 'val2', 'key3' : 'val3', 'key4' : 'val4'}
my_dict2 = {'key11' : 'val11', 'key22' : 'val22', 'key33' : 'val33', 'key44' : 'val44'}
my_dict.update(my_dict2)
print(my_dict)


# 10. dict.values() = Returns a list of dictionary's values
print('# 10.')
my_dict = {'key1' : 'val1', 'key2' : 'val2', 'key3' : 'val3', 'key4' : 'val4'}
print(my_dict.values())
print(list(my_dict.values()))