def first_non_repeating(str):
    n=len(str)

    for i in range(0,n):
        count=1
        for j in range(0,n):
            if(str[i]==str[j]):
                count=count+1


        if(count==2):
            print(str[i])
            break

str="SARTHAK"
p=first_non_repeating(str)
print(p)

