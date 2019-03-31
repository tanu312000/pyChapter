# class Book:
#     def setData(self):
#         self.name=input("Enter Name")  #Parameterised Passing
#         self.author=input("Enter Name")
#         self.price=float(input("Enter price"))
#
#     def display(self):
#         print(self.name)
#         print(self.author)
#         print(self.price)
#
# b=Book()
# b2=Book()
# b.setData()
# b.display()
# b2.setData()
# b2.display()

# class Addition:
#     def init(self,a,b):
#         self.a=a
#         self.b=b
#
#     def add(self):
#         self.c=self.a+self.b
#
#     def display(self):
#         print(self.a)
#         print(self.b)
#         print(self.c)
#
# a1=Addition()
#
# a1.init(10,12)
# a1.add()
# a1.display()


class Counter:
    x = 10  # static

    def incr(self):
        Counter.x = Counter.x + 1
        print(Counter.x)


c1 = Counter()
c2 = Counter()
c3 = Counter()

c1.incr()
c2.incr()
c3.incr()