
# This program shows multiple inheritance

# Create a base class 1

class Base1:
    def __init__(self,a):
        self.a = a

    def MessageFromBase1(self):
        print "This is base class 1"

# Create a base class 2
class Base2:
    def __init__(self,b):
        self.b = b

    def MessageFromBase2(self):
        print "This is base class 2"

# Create a derived class from base class 1 and base class 2  - multiple inheritance

class Derived(Base1,Base2):
    def __init__(self,c):
        Base1.__init__(self,a)
        self.a = c

    def MessageFromDerived(self):
        print "This is derived class"


callBase1 = Base1()
callBase2 = Base2()
callDerived = Derived()

callBase1.MessageFromBase1()
callBase2.MessageFromBase2()
callDerived.MessageFromBase2()
callDerived.MessageFromDerived()