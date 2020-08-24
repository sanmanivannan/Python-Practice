class Human:   # Creating a new class with a name Human
    def __init__(self, n , o): # creating a first PROPERTY of the class Human, This is also called as the constructor
        self.name = n
        self.occupation = o

    def do_work(self): # creating a first METHOD/FUNCTION under the class Human
        if self.occupation == "Tennis":
         print(self.name, "He/She is a Player")
        elif self.occupation == "Acting":
         print(self.name, "He/She is a Actor")

    def speak(self):  # creating a second METHOD/FUNCTION under the class Human
        print(self.name, " He/She can Speak")

#Creating a OBJECT out of the Class Human
tom = Human("Tom", "Acting")
tom.do_work()
tom.speak()

sam = Human("Sam", "Tennis")
sam.do_work()
sam.speak()
