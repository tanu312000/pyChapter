class getmin:
    def push(self, x):
        if (len(self.stack1) == 0):
            self.stack1.append(x)
            self.stack2.append(x)
        else:
            self.stack1.append(x)
            if (self.stack1[top] <= self.stack2[-1]):
                self.stack2.append(x)
            else:
                self.stack2.append(self.stack2[-1])

    # @return nothing
    def pop(self):
        if (len(self.stack1) != 0):
            self.stack1.pop()
            self.stack2.pop()

    # @return an integer
    def top(self):
        if (len(self.stack1) == 0):
            return -1
        else:
            return self.stack1[-1]
        def getMin(self):
            if (len(self.stack1) == 0):
                return -1
            else:
                return self.stack2[-1]