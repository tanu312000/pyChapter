import csv

with open("/home/tanu/programs/pythonFiles/empdetails.csv",'r') as csvFile:
    data=csv.DictReader(csvFile)

    with open("/home/tanu/programs/pythonFiles/emp1details.csv",'w') as csvFile2:
        fieldnames=['eno','name','sal','gender','dno']
        wdata=csv.DictWriter(csvFile2,fieldnames=fieldnames,delimiter=',')
        wdata.writeheader()

        for line in data:
            wdata.writerow(line)


