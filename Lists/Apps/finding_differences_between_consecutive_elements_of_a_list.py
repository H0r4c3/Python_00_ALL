'https://stackoverflow.com/questions/2400840/python-finding-differences-between-elements-of-a-list?noredirect=1&lq=1'

def finding_differences(my_list):
    diff = [abs(j-i) for i,j in zip(my_list, my_list[1:])]
    
    return diff


def check_neighbors(my_list):
    '''Check if differences are 0 or 1'''
    diff = [abs(j-i) for i, j in zip(my_list, my_list[1:])]
    
    return all(item == 0 or item == 1 for item in diff)


my_list = [1, 2, 4, 7, 11, 111]
my_list = [1, 2, 2, 3, 3, 3, 4]
diff = finding_differences(my_list)
print(diff)

check_n = check_neighbors(diff)
print(check_n)