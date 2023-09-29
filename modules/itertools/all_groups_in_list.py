from itertools import combinations_with_replacement, permutations

my_list = [1, 2, 3, 4, 5]

my_list = [1, 2, 3]

print(f'combinations_with_replacement(my_list, 3):')
print(list(combinations_with_replacement(my_list, 3)))
print()
print(f'list(permutations(my_list, 3):')
print(list(permutations(my_list, 3)))

# BEST BEST BEST
# doing permutations for every tuple in combinations_with_replacements
all_combs = list()
for item in combinations_with_replacement(my_list, 3):
    perm_item = set(permutations(item, 3))
    print(perm_item)
    all_combs.extend(perm_item)
    
print(all_combs)