'''#WAP to read line by line from keyboard & append to a list until n times. Break the loop under break condition.

#Step:1
# 1)ReadLine from keyboard

Line=input("Enter a Line"+"\n")

# 2)Append in the list

li=[]
li.append(Line)

# 3)Until n times

while True:
    Status=input("Do you want to continue")

# 4)Break the condition

if(Status=="no"):
    break
    print("Success")
# 5)Write in a file'''

fp=open("/home/tanu/programs/pythonFiles/AppendFile.txt",'a')
li=[]

while True:
    Line=(input("Enter a line")+"\n")
    li.append(Line)
    Status=input("Do you want to Continue")
    if(Status=="No"):
        print("Success")
        break

fp.writelines(li)
fp.close()


