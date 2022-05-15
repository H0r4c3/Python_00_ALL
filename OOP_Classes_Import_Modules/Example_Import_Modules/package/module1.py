
from module2 import Account2


class Account1:
    def __init__(self, username1, password1):
        self.username1 = username1
        self.password1 = password1

    def method1(self):
        print("username1: ", self.username1)
        print("password1: ", self.password1)


def main():
    employee1 = Account1('u1 in module1', 'pw1 in module1')
    employee2 = Account2('u2 in module1', 'pw2 in module1')

    employee1.method1()
    employee2.method2()

if __name__ == "__main__":
    main()