class Beverage:
    # this is a docustring explaining what this class is for. This is a beverage class with attributes and methods
    def coffee(self):
        print "You ordered for Coffee!!"

    def tea(self):
        print "You ordered for Tea!!"

# creating object of class Beverage
drink = Beverage()

# calling the methods inside the class
print Beverage.coffee
# even when there is no parameter is passed this method is executed as "Self" is the first parameter passed
print drink.tea