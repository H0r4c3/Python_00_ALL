'https://www.w3resource.com/python-exercises/challenges/1/python-challenges-1-exercise-24.php'

'''
Write a Python program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, ...
shows the first 10 ugly numbers.
Note: 1 is typically treated as an ugly number.
'''

def is_ugly_number(n):
    if n == 0:
        return False
        
    for i in [2, 3, 5]:
        print(f'i = {i}')
        while n % i == 0:
            n = n/i
            print(f'n = {n}')
    
    if n == 1:
        return True
    else:       
        return False

n = 15353535353
print(is_ugly_number(n))
    