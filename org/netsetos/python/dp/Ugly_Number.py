def getUglyNumber(num):
    ugly=[0]*num
    i2=0
    i3=0
    i5=0

    next_multiple_2=2
    next_multiple_3 = 3
    next_multiple_5 = 5
    next_Ugly_Number=1

    ugly[0]=1

    for index in range(1,num):
        ugly[index]=min(next_multiple_2,next_multiple_3,next_multiple_5)



        if(ugly[index]==next_multiple_2):
            i2=i2+1
            next_multiple_2=ugly[i2]*2

        if (ugly[index] == next_multiple_3):
            i3 = i3 + 1
            next_multiple_3 = ugly[i3] * 3

        if (ugly[index] == next_multiple_5):
            i5 = i5 + 1
            next_multiple_5 = ugly[i5] * 5

    return ugly[index]

t=getUglyNumber(10)
print(t)



