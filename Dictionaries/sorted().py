
d = {1 : 20, 2 : 30, 3 : 16, 4 : 15}

# sorting a dictionary after values
d1 = sorted(d.items(), key = lambda x: x[1], reverse=True)
print(d1)


# obtaining a list with the sorted values
d2 = sorted(d.values())
print(d2)


# obtaining a list with the sorted keys
d3 = sorted(d)
print(d3)


# obtaining a list with the keys
print(list(d))


# obtaining a list with the values
print(list(d.values()))

# obtaining a list of tuples (key, value)
print(list(d.items()))