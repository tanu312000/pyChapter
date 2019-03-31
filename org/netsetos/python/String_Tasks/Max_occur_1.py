ASCII_SIZE=256
def Max_occur_char(str):
    count=[0]*ASCII_SIZE

    max=0
    c=''
    for i in str:
        count[ord(i)]+=1

    for i in str:
        if(max< count[ord(i)]):
            max = count[ord(i)]
            c=i

    return c


str="SARTHAK TANU"

print("Max occuring character is",Max_occur_char(str))
