# class Solution:
#     def deleteDuplicates(self, head):
#         cur = head
#         while cur:
#             if cur.next and cur.next.val == cur.val:
#                 cur.next = cur.next.next
#             else:
#                 cur = cur.next
#         return head


# def bar(x,y):
#     if(y==0):
#         return 0
#     return (x+bar(x,y-1))
#
# def foo(x,y):
#     if(y==0):
#         return 1
#     return bar(x,foo(x,y-1))
#
# test=foo(3,5)
# print(test)


def solve(A,B):
    result=A*[0]
    size=len(B)

    for i in range(size):
        row1=B[i]
        if(len(row1)>=3):
            firstIndex=row1[0]-1
            secondIndex=row1[1]-1
            price=row1[2]
            for j in range(firstIndex,secondIndex+1):

                result[firstIndex]=result[firstIndex]+price
                # result[secondIndex]=result[secondIndex]+price
                firstIndex=firstIndex+1
                # secondIndex=secondIndex+1
    return result


B=[[1,2,10],[2,3,20],[2,5,25]]
A=5
test=solve(A,B)
print(test)