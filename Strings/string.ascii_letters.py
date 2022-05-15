import string

i = 0
for letter in string.ascii_letters:
    print("The letter at index %i is %s" % (i, letter))
    i = i + 1