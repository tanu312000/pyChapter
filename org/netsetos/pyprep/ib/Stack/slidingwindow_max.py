def slidingMaximum(A, B):
    if(not A):
        return A
    st = []
    for i in range(B):
        while st and A[st[-1]] <= A[i]:
            st.pop()
        st.append(i)

    l = [A[st[0]]]

    n = len(A)
    for i in range(B, n):
        while st and A[st[-1]] <= A[i]:
            st.pop()
        while st and i - st[0] >= B:
            st.pop(0)
        st.append(i)
        l.append(A[st[0]])

    return l

A=[1,3,-1,-3,5,3,6,7]
B=3
test=slidingMaximum(A,B)
print(test)