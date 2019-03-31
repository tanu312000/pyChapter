def run_length_encoding(str):
    n=len(str)
    count = 1
    for i in range(0,n-1):
        if(str[i]==str[i+1]):
            count=count+1
        else:
            print(str[i],count)
            count=1

def run_length_encoding1(str):
    n = len(str)
    i=0
    while(i<n):
        count = 1
        while(i<n-1 and str[i]==str[i+1]):
            count=count+1
            i=i+1
        print(str[i], count)
        i=i+1





str="SSSSSMMMAAARRRRTTTT"
d=run_length_encoding(str)
print(d)