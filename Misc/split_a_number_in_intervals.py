

s = 10000 # superior limit
n = 10 # number of parts

part = s // n # length of each part
part = 1000
parts = []

parts = [(i, i + part) for i in range(0, s, part)]

print(parts)