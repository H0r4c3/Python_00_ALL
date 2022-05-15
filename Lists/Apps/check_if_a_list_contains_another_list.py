
def list_contains_list_(small, large):
    #index = str(large).index(str(small))
    s = ''.join(map(str, small))
    l = ''.join(map(str, large))
    index = l.index(s)
    
    print(index)
    return index


def list_contains_list(small, large):
    index_list = list()
    a = len(small)
    b = len(large)
    for i in range(0, b, 1):
        print(large[i : i+2])
        if small == large[i : i+2]:
            index_list.append(i)

    print(index_list)
    return index_list


# find 'small' list in 'large' list and replace 0 with 2, and 1 with 3
def list_contains_list_and_replace(small, large):
    index_list = list()
    a = len(small)
    b = len(large)
    small_replace = [2 if item == 0 else 3 for item in small]
    for i in range(0, b, 1):
        print(large[i : i+2])
        if small == large[i : i+a]:
            index_list.append(i)
            large = large[:i] + small_replace + large[i+2 : ]
            print(large)

    print(large)
    print(index_list)
    return index_list


small = [0, 1]
large = [4, 5, 0, 1, 5, 8, 4, 0, 1, 5, 9]

index_list = list_contains_list_and_replace(small, large)
print(index_list)