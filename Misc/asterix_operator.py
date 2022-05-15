'https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/?__s=9sds60aihy1vkjawrnya'

'''
In Python 3.0, the * operator was added to the multiple assignment syntax, allowing us to capture remaining items after an unpacking into a list:

'''

numbers = [1, 2, 3, 4, 5, 6]
first, *rest = numbers

print(first)
print(rest)

head, *middle, tail = numbers
print(head)
print(middle)
print(tail)