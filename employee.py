import csv

f=open("/home/tanu/programs/pythonFiles/employe.csv",'r')
emp=csv.reader(f)
for i in emp:
    print(i)

f.close()