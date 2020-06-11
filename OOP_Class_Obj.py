class Parrot:
    #Class variable /attribute
    species = "Bird"

    # init function to initialize variable
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sing(self,song):
        return "{} is singing {}".format(self.name,song)

    def dance(self):
        return "{} is now dancing".format(self.name)




blu = Parrot("Blu",10)
woo = Parrot("Woo", 15)


print   blu.__class__.species
print woo.__class__.species

print blu.name,blu.age
print woo.name,woo.age

print blu.sing("Happy")
print woo.dance()
