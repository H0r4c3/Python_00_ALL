


from pandas.core.common import flatten

my_list = [0, 1, [2, 3, [4, 5]]]
print(list(flatten(my_list)))
# [0, 1, 2, 3, 4, 5]