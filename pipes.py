import csv

csv.register_dialect('pipes',delimiter='-')
with open("/home/tanu/programs/pythonFiles/removepipes.csv",'r') as f:
    reader=csv.reader(f,dialect='pipes')
    for row in reader:
        print(row)
