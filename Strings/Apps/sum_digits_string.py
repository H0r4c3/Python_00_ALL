

def sum_digits_string(str1):
    sum_digit = 0
    for x in str1:
        if x.isdigit() == True:
            z = int(x)
            sum_digit = sum_digit + z

    return sum_digit


def sum_digits_string2(s):
    sum_digits = 0
    for x in s:
        if x == 'a':
            z = 10
        elif x == 'b':
            z = 11
        elif x == 'c':
            z = 12
        elif x == 'd':
            z = 13
        elif x == 'e':
            z = 14
        elif x == 'f':
            z = 15
        else:
            z = int(x)
            
        sum_digits = sum_digits + z

    return sum_digits


def sum_digits_string3(nr):
    sum_digits = 0

    for i in hex(nr)[2:]:
        sum_digits += int(i, 16)

    return sum_digits


result = sum_digits_string2('1a2')
print(result)
result = sum_digits_string3(418)
print(result)