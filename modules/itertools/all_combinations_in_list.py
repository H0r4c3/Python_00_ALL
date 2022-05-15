from itertools import combinations

def all_combinations(s):
    all_comb_list = list()
    li = list()
    
    all_comb_list = [list(item) for i in range(1, len(s)+1) for item in combinations(s, i)]
    
    return all_comb_list


s = [1, 2, 3, 4]
all_comb_list = all_combinations(s)
print(all_comb_list)


all_comb_dict = dict()    
for i in range(1, len(s)+1):
    all_comb_dict[i] = list(combinations(s, i))
    
print(all_comb_dict)
