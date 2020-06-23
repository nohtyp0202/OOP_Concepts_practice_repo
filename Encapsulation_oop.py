# ENCAPSULATION
# protected members - prefixed by single "_" underscore
class Base:
    def __init__(self):
        self._a = 2 # this is a protected member of base class
        self._num = 4

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print "Printing the protected member from the base class"
        print self._a # Protected member can be accessed in the class and derived classes but not outside the class
        self.num2 = self._num * 4


obj1 = Derived()
obj2 = Base()

#print obj2.a
# this statement will throw "AttributeError:" as protected variable is being accessed outside the class

print obj1.num2