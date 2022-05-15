'Get all the positions in just one line'

my_string = 'Hello'
to_find = 'l'

# in one line
print([i for i, x in enumerate(my_string) if x == to_find])




def find_indexes(my_string, to_find):
    indexes_list = [i for i, x in enumerate(my_string) if x == to_find]
    return indexes_list

indexes_list = find_indexes('abcadefablmna', 'a')
print(indexes_list)

