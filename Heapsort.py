import math
def max_heapify(A,currentNode):
    print(currentNode)
    left=2*currentNode+1
    right=2*currentNode+2
    largest=currentNode

    if(left<=len(A)-1 and A[left]>A[currentNode]):
        largest=left


    if(right<=len(A)-1 and A[right] > A[largest]):
        largest=right

    if(largest!=currentNode):
        temp=A[currentNode]
        A[currentNode]=A[largest]
        A[largest]=temp
        max_heapify(A, largest)






def Build_max_heapify(A):
    for i in range(math.floor(((len(A))/2)-1),-1,-1):
        max_heapify(A,i)

def heap_extract_max(A):
    if len(A)<0:
        Error="Heap Underflow"
    max=A[0]
    A[0]=A[len(A)-1]
    max_heapify(A,0)
    return max

def heap_increase_key(A,node,value):
    if(value<A[node]):
        print("Error")
    A[node]=value
    parentNode=math.floor((node-1)/2)
    while(node>0 and A[parentNode] < A[node]):
        temp=A[node]
        A[node]=A[parentNode]
        A[parentNode]=temp

        node=parentNode
        parentNode = math.floor((node - 1) / 2)


def min_heapify(A,currentNode):

    left=2*currentNode+1
    right=2*currentNode+2
    smallest=currentNode

    if(left<=len(A)-1 and A[left]<A[currentNode]):
        smallest=left


    if(right<=len(A)-1 and A[right] < A[smallest]):
        smallest=right

    if(smallest!=currentNode):
        temp=A[currentNode]
        A[currentNode]=A[smallest]
        A[smallest]=temp
        min_heapify(A, smallest)

def Build_min_heapify(A):
    for i in range(math.floor(((len(A))/2)-1),-1,-1):
        min_heapify(A,i)


def heap_extract_min(A):
    if len(A)<0:
        Error="Heap Underflow"
    min=A[0]
    A[0]=A[len(A)-1]
    min_heapify(A,0)
    return min

def heap_decrease_key(A,node,value):
    if(value<A[node]):
        print("Error")
    A[node]=value
    parentNode=math.floor((node-1)/2)
    while(node>0 and A[parentNode] > A[node]):
        temp=A[node]
        A[node]=A[parentNode]
        A[parentNode]=temp

        node=parentNode
        parentNode = math.floor((node - 1) / 2)



A=[16,10,8,7,6,5,4,2]
#Build_max_heapify(A)
#max_heapify(A,0)
#max1=heap_extract_max(A)
#print(max1)
Build_min_heapify(A)
#heap_extract_min(A)
heap_decrease_key(A,7,1)
#heap_increase_key(A,7,18)
# print(A[:len(A)-1])
print(A)



