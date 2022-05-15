from itertools import combinations

def split_list(my_list):
    left, right = list(), list()
    all_comb = list()
    pairs = list()
    
    for i in range(1, len(my_list)):
        all_comb = all_comb + list(combinations(my_list, i))
    
    for item in all_comb:
        left = item
        right = my_list[:]
        for i in left:
            right.remove(i)
        pairs.append([left, right])
        
    return pairs

my_list = [1, 2, 3, 4, 5, 5]

pairs = split_list(my_list)
print(pairs)