

my_string = 'AĂÂSŞTŢ'
my_list = ['A', 'Ă', 'Â', 'S', 'Ş', 'T', 'Ţ']

my_ord_list = sorted(my_list)
my_ord_string = ''.join(sorted(my_string))
print(my_ord_list)
print(my_ord_string)

#for char in my_ord_string:
#    print(ord(char))
