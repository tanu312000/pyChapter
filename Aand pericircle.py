class Circle:
    def init(self,r):
        self.r = r


    def area(self):
        self.c = 3.14*self.r*self.r

    def perimeter(self):
        self.d=2*3.14*self.r

    def display(self):
        print(self.c)
        print(self.d)


if (__name__ == '__main__'):
    c1 = Circle()

    c1.init(2)
    c1.perimeter()
    c1.area()
    c1.display()