'https://favtutor.com/blogs/merge-dictionaries-python'

'''
Merge 2 dictionaries having same keys and as values having lists
'''

# Method 1

def merge_two_dictionaries1(d1, d2):
    d = d1.copy()
    
    for v1, v2 in zip(d.values(), d2.values()):
        v1.extend(v2)
        v1.sort()

    return d

d1 = {1: [1], 2: [3], 3: [2, 4], 4: [3], 5: [6], 6: [5, 7], 7: [6, 8], 8: [7, 9], 9: [8]}
d2 = {1: [3], 2: [6], 3: [1], 4: [8], 5: [], 6: [2], 7: [], 8: [4], 9: []}

d = merge_two_dictionaries1(d1, d2)
print(d)


# Method 2

def merge_two_dictionaries2(d1, d2):
    d = {key: (value1, value2) for key, value1, value2 in zip(d1.keys(), d1.values(), d2.values())}
    
    return d

d1 = {1: [1], 2: [3], 3: [2, 4], 4: [3], 5: [6], 6: [5, 7], 7: [6, 8], 8: [7, 9], 9: [8]}
d2 = {1: [3], 2: [6], 3: [1], 4: [8], 5: [], 6: [2], 7: [], 8: [4], 9: []}

d = merge_two_dictionaries2(d1, d2)
print(d)


# Method 3

def merge_two_dictionaries3(d1, d2):
    d = {key: value1 + value2 for key, value1, value2 in zip(d1.keys(), d1.values(), d2.values())}
    
    return d

d1 = {1: [1], 2: [3], 3: [2, 4], 4: [3], 5: [6], 6: [5, 7], 7: [6, 8], 8: [7, 9], 9: [8]}
d2 = {1: [3], 2: [6], 3: [1], 4: [8], 5: [], 6: [2], 7: [], 8: [4], 9: []}

d = merge_two_dictionaries3(d1, d2)
print(d)