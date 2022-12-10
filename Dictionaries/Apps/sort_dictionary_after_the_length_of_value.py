my_dict = {3:[1, 2, 3], 1:[1], 4:[1, 2, 3, 4], 2:[1, 2]}
print(my_dict.items())

sorted_key_value_pairs = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
print(sorted_key_value_pairs)

# Recreate the dictionary, now, sorted
new_dict = {key:value for key, value in sorted_key_value_pairs}
print(new_dict)