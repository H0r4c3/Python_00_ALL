'https://therenegadecoder.com/code/how-to-sum-elements-of-two-lists-in-python/'



list1 = [1, 2, 3, 4, 5]
list2 = [9, 8, 7, 6, 5]

# 1. Method: List comprehension

zipped_lists = zip(list1, list2)
sum1 = [x + y for (x, y) in zipped_lists]
print(sum1)


# 2. Method: Sum Elements of Two Lists with a Mapping

import operator

sum2 = list(map(operator.add, list1, list2))
print(sum2)


# 3. Method: Loop

sum3 = []

for i in len(list1):
    sum3.append(list1[i] + list2[i])
    
print(sum3)