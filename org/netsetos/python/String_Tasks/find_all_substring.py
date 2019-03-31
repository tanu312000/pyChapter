def find_all_substring(str,n):
    for i in range(1,n+1):
        for j in range(0,n-i+1):
            k=i+j-1
            for l in range(j,k+1):
                print(str[l],end=" ")

            print()


str="a string containing"
n=4
print(find_all_substring(str,n))