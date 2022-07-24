from class_b_module import ClassB

class ClassA():
    def __init__(self, a):
        self.a = a

    def methodA(self):
        print(self.a)
        return self.a
    
def main():    
    #obj_a = ClassA('aaa')
    #result1 = obj_a.methodA()
    #print(result1)
    
    obj_b = ClassB('imported_b')
    result2 = obj_b.methodB()
    print(result2)


if __name__ == "__main__":
    main()