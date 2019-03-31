class A:
    a = 20

    def f1(self):
        self.a = 30
        a = 40
        print(a)  # 40
        print(self.a)  # 30
        print(A.a)  # 20
    




a1 = A()
a1.f1()