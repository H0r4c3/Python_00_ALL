'Eliminate pairs of equal items from a list (only in pairs, not all'

def eliminate_duplicates(my_list):
    for item in my_list:
        print(item)
        count = my_list.count(item)
        print(count)
        if count >= 2:
            for i in range(1, count // 2 + 1):
                print(item, i)
                my_list.remove(item)
                my_list.remove(item)
                print(my_list)
            
    return my_list


my_list = [1, 2, 2, 2, 3, 4, 4, 4, 4, 4, 5, 5]

new_list = eliminate_duplicates(my_list)
print(new_list)