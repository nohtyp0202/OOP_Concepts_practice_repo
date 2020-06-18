# This program is to show the multilevel inheritance

class BaseClass1:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def sum(self,x , y):
        return x + y

class DerivedClass1(BaseClass1):

    def __init__(self,x,y):
        BaseClass1.__init__(self,x,y)
        self.a = x
        self.b = y
    def product(self,a,b):
        return a * b

class DerivedClass2(DerivedClass1):

    def __init__(self,x,y):
        DerivedClass1.__init__(self,x,y)
        self.p = x
        self.q = y

    def division(self,p,q):
        return p / q


numFunc1 = BaseClass1(2,3)
numFunc2 = DerivedClass1(4,5)
numFunc3 = DerivedClass2(14,7)

print numFunc1.sum(2,3)
print numFunc3.product(4,5) # CALLING FROM DERIVED CLASS 2
print numFunc3.division(14,7) # CALLING FROM DERIVED CLASS 2
