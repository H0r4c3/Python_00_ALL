
number = int(input('Enter a number: '))

number1 = number
list_of_digits = list()

while(number>0):
    d = number % 10
    list_of_digits.append(d)
    number = number // 10

list_of_digits_ok = list_of_digits[::-1]

print(f'Number = {number1}')
print(f'Digits = {list_of_digits_ok}')

# Method 2

number2 = number1

number_string = str(number2)
number_list = list(number_string)

# transform the list of strings into a list of integers
list_of_digits2 = [int(i) for i in number_list]

print(list_of_digits2)
