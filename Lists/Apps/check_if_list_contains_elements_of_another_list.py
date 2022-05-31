'https://www.techbeamers.com/program-python-list-contains-elements/'

# 1. Method

large = [1, 2, 3, 4, 5, 6, 7, 8, 9]
small_ok = [1, 3, 5, 7, 9]
small_nok = [1, 3, 5, 7, 10]

def contains(list1, list2):
    check =  all(item in list1 for item in list2)
    return check

print(contains(large, small_ok))
print(contains(large, small_nok))



# 2. Method

def contains(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    
    if set1.intersection(set2) == set2: 
        return True 
    else: 
        return False

print(contains(large, small_ok))
print(contains(large, small_nok))
