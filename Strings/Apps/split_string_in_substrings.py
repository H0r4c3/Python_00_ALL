'''
Create a list with all substrings from a string
Input = string
Input = the length of substrings
Output = list of substrings
Example: 'abcde' and 3 -> ['abc', 'bcd', 'cde'] 
'''

# my_string = 'abcde'
# substring_length = 3

# # substring1 = my_string[0:3]
# # substring2 = my_string[1:4]
# # substring3 = my_string[2:5]

# # print(substring1)
# # print(substring2)
# # print(substring3)

# my_list = [my_string[i: i+substring_length]
#            for i in range(len(my_string) - substring_length + 1)]
# print(my_list)


def substrings_from_string(my_string, substrings_length):
    my_list = [my_string[i: i+substrings_length]
               for i in range(len(my_string) - substrings_length + 1)]
    print(my_list)


if __name__ == '__main__':
    print('Enter a string: ')
    my_string = input().strip()
    
    print('Enter the length of the substrings: ')
    substrings_length = int(input().strip())

    substrings_from_string(my_string, substrings_length)
