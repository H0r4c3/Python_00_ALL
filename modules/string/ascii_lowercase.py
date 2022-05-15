
from string import ascii_lowercase as alphabet

print(alphabet)

delta = 3
shifted = alphabet[delta:] + alphabet[:delta]
print(shifted)