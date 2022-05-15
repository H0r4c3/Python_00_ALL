'https://www.udemy.com/course/python-complete-course-for-beginners-h/learn/lecture/24345926#overview'


my_list1 = [item for item in range(100) if item % 2 == 0 if item % 5 == 0]
print(my_list1)

my_list2 = ['Even' if item % 2 else 'Odd' for item in range(10)]
print(my_list2)

my_list3 = [[item for item in range(5)] for item in range(3)]
print(my_list3)


# list comprehension with multiple if else
'''
Creating product reviews that take values from 1 to 5 and create a list with three categories:

Good >= greater or equal to 4
Neutral = if the review is 3
Negative < if the review is less than 3
'''
x = [5, 2, 1, 4, 5, 2]

res = ["Good" if i >= 4 else "Neutral" if i == 3 else "Bad" for i in x]

print(res)


# another example
values_string = 'name: "Bob Dylan"\n' 'children: 6\n' 'coding: "null" '
     
values_list = ' '.join((values_string.splitlines()))
     
values_list = [val[1:-1].replace('\\"', '"') if val.startswith('"') and val.endswith('"') 
                   else val.strip('"') if '"' in val 
                   else True if val == 'true' 
                   else False if val == 'false'
                   else None if val in ('null' or not val)
                   else int(val) if val.isnumeric() else val
                   for val in values_list]

print(values_list)


# Example with a function
def f(x): 
    return x % 2 != 0 and x % 3 != 0

[i for i in range(2, 25) if f(i)]