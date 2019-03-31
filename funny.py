fp=open("/home/tanu/programs/pythonFiles/funny.txt",'r')
f_out=open("/home/tanu/programs/pythonFiles/funny2.txt",'w')

for line in fp:
    words=line.split(" ")
    f_out=fp.write(line+str(len(line)))

fp.close()
f_out.close()
