
fp= open("/home/tanu/Downloads/emp.csv",'r')

data=fp.readlines()
for rows in data:
    print(rows,end="")
fp.close()


