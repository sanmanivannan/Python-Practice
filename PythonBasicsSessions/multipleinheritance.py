class Father():
    def gardening(self):
        print("I like gardening")

class Mother():
    def cooking(self):
        print("I like cooking")

class Child1(Father,Mother):
    def art(self):
        print("I like art")

class Child2(Father,Mother):
    def sports(self):
        print("I like sports")
c1 = Child1()
c1.gardening()
c1.art()
c1.cooking()

c2 = Child2()
c2.cooking()
c2.gardening()
c2.sports()
c2.art()





