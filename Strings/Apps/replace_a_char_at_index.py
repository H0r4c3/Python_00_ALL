'replace a portion at a desired index by placing it between "slices" of the original'

my_string = 'StringToBeModified'
replacement_string = 'HHH'
index = 6

modified_string = my_string[:index] + replacement_string + my_string[index + 1:]

print(my_string)
print(modified_string)

my_string = input("Enter your string: ")
replacement_string = input("Enter replacement string: ")
index = input("Enter index for replacement: ")

def replace_in_string(my_string, replacement_string, index):
    index = int(index)
    modified_string = my_string[:index] + replacement_string + my_string[index + 1:]
    return modified_string

print(my_string)
replace_in_string(my_string, replacement_string, index)
print(modified_string)