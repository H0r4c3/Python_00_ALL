'The extend() method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.'

'''
list1.extend(iterable)

Here, all the elements of iterable are added to the end of list1.
'''

# Example 1

# languages list
languages = ['French', 'English']

# another list of language
languages1 = ['Spanish', 'Portuguese']

# appending language1 elements to language
languages.extend(languages1)

print('Languages List:', languages)

# Example 2: Add Elements of Tuple and Set to List

# languages list
languages = ['French']

# languages tuple
languages_tuple = ('Spanish', 'Portuguese')

# languages set
languages_set = {'Chinese', 'Japanese'}

# appending language_tuple elements to language
languages.extend(languages_tuple)

print('New Language List:', languages)

# appending language_set elements to language
languages.extend(languages_set)

print('Newer Languages List:', languages)