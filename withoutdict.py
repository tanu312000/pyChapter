import csv
d={}

keys=['eno','name','sal','gender','dno']
with open("/home/tanu/programs/pythonFiles/empdetails.csv",'r')as csvFile:
    data=csv.reader(csvFile,dialect='mydialect')

    for row in data:
        i=0
        for v in row:
            val=v.split(',')
            for k in val:
                d[keys[i]]=k
                i=i+1

print(d)