
from itertools import combinations
import time

def all_combs(my_string):
    combs_set= set()
    for i in range(len(my_string), 0, -1):
        combs = combinations(my_string, i)
        combs_list = list(map(lambda x: ''.join(x), combs))
        print(combs_list)
        combs_set = combs_set.union(map(lambda x: ''.join(x), combs))
                
    return combs_set

        
    

my_string = 'CGCTA'
#my_string = 'GTCGCTGTGCAGGTCCGGGTTCA'
#my_string = 'GCGACCCGAATCCAGCTATAGGTATATGTCAGTCGGCCGTTAGGT'

start = time.time()
combs_set = all_combs(my_string)
stop = time.time()

print(combs_set)
print(f'Time = {stop - start}')
