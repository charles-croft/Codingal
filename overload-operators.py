class A:
    def __init__ (self,a):
        self.a = a
    def __lt__ (self,other):
        if self.a<other.a:
            print("True")
        else:
            print("False")
    def __eq__ (self,other):
        if self.a==other.a:
            print("True")
        else:
            print("False")
obj1 = A(1)
obj2 = A(2)
obj1 < obj2
obj1 == obj2