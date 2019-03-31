class Person:
    def init(self):
        self.name = "mano"
        self.age = 35
        self.gender = "male"

    def display(self):
        print(self.name)
        print(self.age)
        print(self.gender)


a1 = Person()
a2 = Person()
a3 = Person()
a1.init()
a2.init()
a3.init()

a1.display()
a2.display()
a3.display()