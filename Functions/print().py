# 1. print() without newline

for i in range(6):
    print(i, end='')


print('\n')

for i in range(6):
    print(i)


# 2. print with 2 decimal places

number = 7
print('The number with 2 decimal places is: {:.2f}'.format(number))
print(f'The number with 2 decimal places is: {number:.2f}')


# 3. print with a separator
print(1, 2, 3, 4)
print(1, 2, 3, 4, sep='-')
