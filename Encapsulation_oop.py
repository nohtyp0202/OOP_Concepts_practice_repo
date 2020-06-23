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


#Private members
class BaseClass:
    def __init__(self):
        self.__priv = "I am a private member"
        self.a = "I am not a private member"

    def SomeMethod(self):
        print self.a
        print "Trying to access private member within same class"
        print self.__priv

class DerivedClass(BaseClass):

    def __init__(self):
        BaseClass.__init__(self)
        self.b = "I am a derived class member"


    def SomeOtherMethod(self):
        print self.b
        print "Trying to access public memeber of base class"
        print self.a
        print "Trying to access the private member of the base class,this should throw an error"
        print self.__priv
        #print "Trying data mangaling but using _Classname__private member to still access private members"
        #print self._DerivedClass__priv


print "This is outside the classes"
obj1 = BaseClass()
obj2 = DerivedClass()

obj1.SomeMethod()
obj2.SomeOtherMethod()
