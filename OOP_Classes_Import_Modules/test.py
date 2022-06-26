class Foo:
    def __init__(self):
        self.__bar = 42

foo = Foo()
print(foo._Foo__bar)