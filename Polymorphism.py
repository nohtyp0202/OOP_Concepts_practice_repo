
# polymorphism in python
# same len() gives len but for different datatypes like string, list and dictionary
# same function /method but used for different data types is a type of polymorphism
print len("polymorphism")

print len(["polymorphism", "Inheritance","Abstraction"])


print len({"Double" : "twice", "Triple" : "Trice"})


# Same method names are used in two different classes
# these two classes are not connected to each other
class Rose():
    def color(self):
        print "Roses are RED is color"
    def Grown(self):
        print "Roses grown on land.."

class Lotus():
    def color(self):
        print "Lotus are PINK in color"

    def Grown(self):
        print "Lotus grown on water.."

Flower_rose = Rose()
Flower_lotus = Lotus()

# Because of polymorphism , we can access each method
# inside the two classed by itereating through the tuple of class objects
for flowers in (Flower_rose,Flower_lotus):
    flowers.color()
    flowers.Grown()



# Polymorphism in Inheritence


class Beverage:
    def Intro(self):
        print "There are many hot beverages that are cosumed during winter"

    def Keyquality(self):
        print "Beverages can be hot, sweet and yummy.."

class Coffee(Beverage):
    def Keyquality(self):
        print "Coffee can be hot, sweet and yummy.."

class Tea(Beverage):
    def Keyquality(self):
        print "Tea can be hot, sweet and yummy.."


Bev = Beverage()
Bev_Coffee = Coffee()
Bev_tea = Tea()

Bev.Keyquality()
Bev_Coffee.Keyquality()
Bev_tea.Keyquality()



# polymorphism with functions and objects

class Coffee():
    def Intro(self):
        print "Most of the people in USA drink coffee"
    def Keyquality(self):
        print "Coffee can be hot, sweet and yummy.."

class Tea():
    def Intro(self):
        print "Most of the people in UK drink tea"
    def Keyquality(self):
        print "Tea can be hot, sweet and yummy.."

# creating a function with which methods inside the classes are accessed
def func(obj):
    obj.Intro()
    obj.Keyquality()

# creatin object for the class
obj_coffee = Coffee()
obj_tea = Tea()

# passing objects though the functions to call the methods 
func(obj_coffee)
func(obj_tea)
