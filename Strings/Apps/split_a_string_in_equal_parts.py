
# 1. Method
s = 'abcdefghi'

# k = nr. of parts
k = 3
parts = [s[i:i+k] for i in range(0, len(s), k)]

print(parts)



# 2. Method
import textwrap
parts = textwrap.wrap(s, k)
print(parts)