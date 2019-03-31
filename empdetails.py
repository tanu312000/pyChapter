class Powtow:

    def _init_(self,max=0):
        self.max = max()

    def __iter__(self):
        self.n=0
        return self

    def _next_(self):
        if self.n<=self.max:
            result=2**self.n
            self.n += 1
            return result
        else:
            raise StopIteration

a = Powtow(4)
i=iter(a)
print(next(i))
