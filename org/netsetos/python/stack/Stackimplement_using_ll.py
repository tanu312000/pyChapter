class Node:     #Stackimplement_using_arr
    def __init__(self,data):
        self.data=data
        self.next=None

    def property(self):
        print('papa property')

class StackP:
    def __init__(self):
        self.head=None

    def push(self,data):
        if(self.head == None):
            self.head=Node(data)
            np=Node(12)
            np.pr
        else:
            new_Node=Node(data)
            new_Node.next=self.head
            self.head=new_Node
        print(self.head.data)

    def pop(self):
        if(self.head == None):
            return None
        else:
            temp=self.head.data
            self.head=self.head.next
        print('delete--',temp)
        return temp


if __name__ == "__main__":
    fp = StackP()
    fp.push(10)
    fp.push(20)
    fp.push(30)
    fp.push(40)
    fp.push(50)
    fp.push(60)
    fp.push(70)
    fp.pop()
    fp.pop()
    fp.pop()
    fp.pop()


#Stackimplement_using_ll


