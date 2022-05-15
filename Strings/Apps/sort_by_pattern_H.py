'Sort a string using a pattern'

def sort_by_pattern(my_string):
    pattern = 'AĂÂBCDEFGHIÎJKLMNOPQRSŞTŢUVWXYZ'
    list_my_string_positions = []
    list_my_string_positions_ord = []
    list_my_string_ord = []
    my_string_ord = ''

    # create a list with positions of chars from my_string in pattern
    for char in my_string:
        list_my_string_positions.append(pattern.index(char))

    # sort the positions in pattern
    list_my_string_positions_ord = sorted(list_my_string_positions)

    # create a list with the chars in sorted positions
    for index in list_my_string_positions_ord:
        list_my_string_ord.append(pattern[index])

    # transform the list in string
    my_string_ord = ''.join(list_my_string_ord)
    
    return my_string_ord

my_string1 = 'DEFABCZZĂÂ'
my_string2 = 'ÂAĂBCDŞEÎFŢGHIĂJÎKŞLMNĂOPQRÂSTŢUVWXYZÂ'

my_string_ord = sort_by_pattern(my_string2)

print(my_string_ord)

