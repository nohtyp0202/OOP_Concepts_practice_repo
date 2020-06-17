class ComplexNumber:
    def __init__(self,r = 0,i = 0 ):
        self.real = r
        self.img = i
    def get_data(self):
        print self.real , self.img

# creating a complex number by call class method
# create an instance of class or object
num1 = ComplexNumber(2,3)
num1.get_data()

num2 = ComplexNumber(5)
num2.get_data()

#creating an attribute
num2.attr = 10
print num2.real,num2.img,num2.attr

# deleting an attribute of the object
del num1.img
num1.get_data()

# deleting the object itself
del num1
print num1.get_data()

# Automatic destruction of unreferenced objects in Python is also called garbage collection.


