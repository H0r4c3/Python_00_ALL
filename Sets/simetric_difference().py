

my_set1 = {1, 2, 3, 4, 5}
my_set2 = {5, 6, 7, 8, 9}
print(my_set1.symmetric_difference(my_set2)) # elements in first set or in second set, but not in both
print(my_set2.symmetric_difference(my_set1)) # elements in first set or in second set, but not in both
print(my_set1 ^ my_set2) # simetric difference
print(my_set2 ^ my_set1) # simetric difference