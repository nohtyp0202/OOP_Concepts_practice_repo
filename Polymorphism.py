
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
