# items in list2 that are in list1, too

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [2, 5, 9, 10]

common_items1 = [items in list1 for items in list2]
common_items2 = [items for items in list1 if items in list2]
print(common_items1)
print(common_items2)