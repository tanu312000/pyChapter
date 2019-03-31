#Prog1:to read an entire file

def read_file(wholefilepath,mode):
    fp=open(wholefilepath,mode)
    data=fp.read()
    print(data)
    fp.close()
    print(wholefilepath)

#Prog2:to read n lines
def read_lines(wholefilepath,lines):
    fp=open(wholefilepath,'r')
    datainarray=fp.readlines()
    for line in range(0,lines):
        print(datainarray[line],end="")
#prog3:Appendfile
def append_file(wholefilepath,mode):
    fp=open(wholefilepath,mode)
    successfuldata=fp.write("Teacher told to frank was wrong")
    print(successfuldata)
    fp.close()

read_file("/home/tanu/programs/pythonFiles/funny.txt","r")
#read_file("/home/tanu/programs/pythonFiles/funny_wc.txt","r")

#read_lines("/home/tanu/programs/pythonFiles/funny.txt",7)
#append_file("/home/tanu/programs/pythonFiles/funny.txt","a")