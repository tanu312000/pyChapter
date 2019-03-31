import math
def Compare_Versions(v1,v2):
    v1 , v2 = (map(int, v.split('.')) for v in (v1 , v2))
    d = len(v2) - len(v1)
    a=v1 + [0] * d
    b=v2 + [0] * -d
    return math.cmp(a,b)



test=Compare_Versions(1.2,1.13)
print(test)