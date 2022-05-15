
class Account2:
    def __init__(self, username2, password2):
        self.username2 = username2
        self.password2 = password2

    def method2(self):
        print(self.username2)
        print(self.password2)


def main():
    e2 = Account2('u2 in module2', 'pw2 in module2')

    e2.method2()

if __name__ == "__main__":
    main()