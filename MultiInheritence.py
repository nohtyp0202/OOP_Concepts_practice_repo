
# This program shows multiple inheritance

# Create a base class 1

class Base1:

    def MessageFromBase1(self):
        print "This is base class 1"

# Create a base class 2
class Base2:

    def MessageFromBase2(self):
        print "This is base class 2"

# Create a derived class from base class 1 and base class 2  - multiple inheritance

class Derived(Base1,Base2):

    def MessageFromDerived(self):
        print "This is derived class"


callBase1 = Base1()
callBase2 = Base2()
callDerived = Derived()

callBase1.MessageFromBase1()
callBase2.MessageFromBase2()
callDerived.MessageFromBase2()
callDerived.MessageFromDerived()