'https://stackoverflow.com/questions/40158243/find-all-binary-splits-of-a-nominal-attribute/40166673#40166673'

import itertools

def binary_splits(seq):
    for result_indices in itertools.product((0,1), repeat=len(seq)):
        result = ([], [])
        for seq_index, result_index in enumerate(result_indices):
            result[result_index].append(seq[seq_index])
        #skip results where one of the sides is empty
        if not result[0] or not result[1]: continue
        #convert from list to tuple so we can hash it later
        yield map(tuple, result)

def binary_splits_no_dupes(seq):
    seen = set()
    for item in binary_splits(seq):
        key = tuple(sorted(item))
        if key in seen: continue
        yield key
        seen.add(key)

for left, right in binary_splits_no_dupes(['a','b','c','d']):
    print(left, right)