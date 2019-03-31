f=open("/home/tanu/programs/pythonFiles/break.txt",'r',encoding='utf-8')

print(f.seek())
print(f.read(2))
print(f.tell())
print(f.read(3))
print(f.tell())
f.close()