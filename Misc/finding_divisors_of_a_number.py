'https://alexwlchan.net/2019/07/finding-divisors-with-python/'

def get_divisors(n):
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            yield i
    yield n
    

print(list(get_divisors(6)))