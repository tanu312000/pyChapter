class set_get:
    def set_eno(self, eno):
        self.eno = eno

    def get_eno(self):
        return self.eno

    def set_ename(self, ename):
        self.ename = ename

    def get_ename(self):
        return self.ename

    def set_sal(self, sal):
        self.sal = sal

    def get_sal(self):
        return self.sal


emp = set_get()
print(emp.set_eno(10))
print(emp.set_ename('mano'))#prints the address
print(emp.set_sal(1000.00))

