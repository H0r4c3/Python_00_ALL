
# Using generator:
def fibo(n):
    a = 0
    b = 1
    while a < n:
        yield a
        a, b = b, a+b
        
result = fibo(10)
print(result.__next__())
print(next(result))
print(result.__next__())
print(result.__next__())
print(result.__next__())


for i in fibo(10):
    print(i, end=' ')