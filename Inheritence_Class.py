class BaseClass:
    def __init__(self, n):
        self.n = n
        print "This is init from baseclass"

    def baseclass_func(self):
        print "This is from base class function 1"

    def baseclass_func2(self):
        print "This is from baseclass funtion 2"


class DerivedClass(BaseClass):

    def __init__(self):
        print "This is from derived class init func"

    def derivedclass_func(self):
        print "This is derived class function"


c = DerivedClass()

c.baseclass_func2()
c.baseclass_func()
c.derivedclass_func()