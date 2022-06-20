'https://careerkarma.com/blog/python-remove-duplicates-from-list/#:~:text=You%20can%20remove%20duplicates%20from,whose%20duplicates%20have%20been%20removed.'


# Method 1: Remove Duplicates from List using dict.fromkeys()

new_menu = ['Hawaiian', 'Margherita', 'Mushroom', 'Prosciutto', 'Meat Feast', 'Hawaiian', 'Bacon', 'Black Olive Special', 'Sausage', 'Sausage']

final_new_menu = list(dict.fromkeys(new_menu))

print(final_new_menu)
print(sorted(final_new_menu))




# Method 2: Remove Duplicates Using a Set Example

new_menu = ['Hawaiian', 'Margherita', 'Mushroom', 'Prosciutto', 'Meat Feast', 'Hawaiian', 'Bacon', 'Black Olive Special', 'Sausage', 'Sausage']

final_new_menu = list(set(new_menu))

print(final_new_menu)
print(sorted(final_new_menu))