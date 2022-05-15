'https://github.com/parasjain-12/HackerEarth-Solution'
'https://github.com/parasjain-12/HackerEarth-Solution/blob/master/Monk%20and%20Rotation.py'

my_list = [1, 2, 3, 4, 5, 6]
n = len(my_list)
k = 2 # step of rotation
k = k % n # in case k > n

a = my_list[n-k : ]
b = my_list[ : n-k]
c = a + b
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')