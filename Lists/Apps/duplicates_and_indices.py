'https://www.geeksforgeeks.org/python-duplicate-element-indices-in-list/'


my_list = [0, 1, 2, 3, 4, 2, 5, 6, 7, 3, 8]
#my_dict = dict()
duplicates_dict = dict()
distances = list()

# Create enumerate of my_list
# for idx, val in enumerate(my_list):
#     my_dict[idx] = val

i = 0    
def duplicates(my_list):
    # creates a dictionary having as keys the duplicates and as values the indices
    for x in range(i, len(my_list)):
        for y in range(i+1, len(my_list)):
            if (my_list[x] == my_list[y] and x!=y):
                duplicates_dict[my_list[x]] = [x, y]
                
    return duplicates_dict

# def minimum_distance(my_list):
#     # The distance between two array values is the number of indices between them.
#     for x in range(i, len(my_list)):
#         for y in range(i+1, len(my_list)):
#             if (my_list[x] == my_list[y] and x!=y):
#                 distances.append(abs(x-y))
#                 print(abs(x-y))
                
#     return distances

#min_dist = min(distances)
#print(min_dist)
#print(distances)

duplicates_dict = duplicates(my_list)
            
print(duplicates_dict)
        
