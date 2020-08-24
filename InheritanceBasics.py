class Vehicle:
    def general_usage(self):
        print("general usage vehicle:master class")

class Car(Vehicle):
    def __init__(self):    #PROPERTY OR CONSTRUCTOR
        print("I'm a Car")
        self.wheels = 4
        self.roof = True
        print("I have", self.wheels, "wheels and have roof:", self.roof)
    def character(self):   #METHOD INSIDE THE CAR CLASS
        print("printing characteristics of a car:METHOD INSIDE THE CAR CLASS")
        self.general_usage()

class Motorcycle(Vehicle):
    def __init__(self):    #PROPERTY OR CONSTRUCTOR
        print("I'm a Motercycle")
        self.wheels = 2
        self.roof = False
        print("I have", self.wheels, "wheels and have roof:", self.roof)
    def character(self):   #METHOD INSIDE THE CAR CLASS
        print("printing characteristics of a Motorcycle : METHOD INSIDE THE MOTORCYCLE CLASS")
        self.general_usage()

c = Car()  # OBJECT derived from the Car Class
c.character()
#c.general_usage()

m = Motorcycle()  # OBJECT derived from the Motorcycle class
m.character()
#m.general_usage()