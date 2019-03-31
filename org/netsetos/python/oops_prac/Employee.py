class Employee:
    # eno,ename,sal
    def set_eno(self, eno):
        self.__eno = eno

    def get_eno(self):
        return self.__eno

    def set_ename(self, ename):
        self.__ename = ename

    def get_ename(self):
        return self.__ename

    def set_sal(self, sal):
        self.__sal = sal

    def get_sal(self):
        return self.__sal

# private member can be accessed only within class
emp = Employee()
emp.set_eno(10)
emp.set_ename('mano')
emp.set_sal(1000.00)

print(emp.get_eno())
print(emp.get_ename())
print(emp.get_sal())










