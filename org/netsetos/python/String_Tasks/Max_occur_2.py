def Max_occur_char(A):

    curr_count=1
    max_count_so_far=1
    Max_occur_char=A[0]
    n=len(A)
    for i in range(0,n):
        for j in range(i+1,n):
            if(A[i]==A[j]):
                curr_char=A[i]
                curr_count=curr_count+1
                if(curr_count>max_count_so_far):
                    max_count_so_far=curr_count






A="SARTHAK TANU"
print("Max occuring character is",Max_occur_char(str))