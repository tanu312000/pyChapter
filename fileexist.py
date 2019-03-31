import os,sys
fname=input("Enter filename")

if os.path.isfile(fname):
    print("File Exists: ",fname)
    f=open(fname,'r')
else:
    print("File does not exists:",fname)
    sys.exit(0)

    print("The content of file is:")
    data = f.read()
    print(data)
f.close()





