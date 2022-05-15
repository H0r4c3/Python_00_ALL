'https://www.geeksforgeeks.org/python-pair-iteration-in-list/'

my_list = [0, 1, 2, 3, 4, 5]

result = list(zip(my_list, my_list[1:] + my_list[:1]))
print(result)