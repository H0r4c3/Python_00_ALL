'https://www.hackerrank.com/challenges/python-string-formatting/problem'


def print_formatted(number):
    w = len("{0:b}".format(number))
    for i in range(1,n+1):
        o=oct(i)
        h=hex(i)
        b=bin(i)
        o=o.replace("0o","")
        h=h.replace("0x","")
        b=b.replace("0b","")
        print(str(i).rjust(w),o.rjust(w),h.upper().rjust(w),b.rjust(w))
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)