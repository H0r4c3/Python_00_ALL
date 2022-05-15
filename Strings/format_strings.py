'https://www.w3schools.com/python/ref_string_format.asp'


# Example 1
# print a number having every 3 decimal places should be separated by a whitespace

def decimal_places(number):
    return f'{number:,}'.replace(',', ' ')

my_number = decimal_places(643903)
print(my_number)


# Example 2
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))