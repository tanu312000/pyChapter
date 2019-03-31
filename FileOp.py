import sys
def readl(pathoffilename):
    if (__name__ == '__main__'):
        print(10)

    file_name = sys.argv[1]
    text = []
    try:
        fh = open(file_name, 'r')
        text = fh.readlines()
        fh.close()
    except IOError:
        print('cannot open', file_name)

    if text:
        print(text)



# txt=eval(input("Enter your input: "))
# print("Recieved input is: ",txt)

print(eval('[x*5 for x in range(2,10,2)]'))
print(eval('[2+2]'))
print(eval('[Hello]'))


f=open("home/tanu")
