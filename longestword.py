fp=open("/home/tanu/programs/pythonFiles/longest.txt","r")

data=fp.read()
line=data.split("\n")
countarray=[]
for i in range(len(line)):
    word=line[i]
    print(word,len(word))
    countarray.append(len(word))

print(countarray)

for j in range(len(countarray)):
    for k in range(j+1,len(countarray)):
        if (countarray[j] > countarray[k]):
            t=countarray[j]
            countarray[j]=countarray[k]
            countarray[k]=t

print(countarray)
x=len(countarray)
print("longest word",countarray[x-1])

















fp.close()