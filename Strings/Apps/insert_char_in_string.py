'''
Insert a char in a string in a given position
'''

def insert_char_in_string(string, position, character):
    new_string = string[:position] + character + string[position:]
    
    return new_string
    
new_string = insert_char_in_string('abcdef', 3, 'H')

#print(f'The old string is: abcdef')
#print(f'The new_string is: {new_string}')

# insert a char in a string repeatedly from position to position
def insert_char_in_string_multiple_positions(string, position, character):
    length = len(string)
    new_string = string
    my_position = position
    position_counter = 0
    while position_counter<length-position:
        new_string = new_string[:my_position] + character + new_string[my_position:]
        print(position_counter)
        print(new_string)
        position_counter = position_counter + position
        my_position = my_position + position + 1
        
    return new_string

new_string = insert_char_in_string_multiple_positions('abcdefghijklmnopqrstuvwxyz', 3, 'H')
print(f'The final string is: {new_string}')
    