# class Counter:
#     x = 10
#
#     @staticmethod
#     def incr():
#         Counter.x = Counter.x + 1
#         print(Counter.x)
#
#
# Counter.incr()  # 11
#
#
#
class A:
    name="Tanu"
    age=24
    def setValues(self):
        self.a = 10
        self.b = 20

    def display(self):
        print(self.a)
        print(self.b)


class B:
    def sum(self):
        self.c = self.a + self.b
        print(self.c)


class C(A,B):
    def mul(self):
        self.result = self.a * self.b
        print(self.result)





c = C()
c.setValues()
c.display()
c.sum()
c.mul()
print(c.__dict__)
print(c.__doc__)

A.__dict__

#we cannot create objects for class








#
# b = Book1('aaa', 'bbb', 700.00)
# b.display()
# b2 = Book1('vvv', 'nnn', 800.00)
# b2.display()
# #
#
# class A:
#     def __del__(self):
#         print("Object destroyed")
#
#
# a1 = A()
# a2 = A()
# a3 = A()
# a4 = A()
# a5 = A()
#
# del a1
# del a2
#
# print("The end")

