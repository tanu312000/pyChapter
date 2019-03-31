def fractionToDecimal(num, den):
    if(den == 0):
        return "NaN"

    if(num*den < 0):
        neg = True
    else:
        neg = False

    num = abs(num)
    den = abs(den)
    s = str(int(num / den))

    remainder = int(num% den)

    if(remainder!=None):
        s =s+'.'

    dict={}

    i = len(s)
    while (remainder!=None):
        num = int(remainder * 10)
        digit = str(int(num/den))

        if(remainder in dict):
            s = s[:dict[remainder]] + "(" + s[dict[remainder]:] + ")"
            break
        else:
            s=s+digit
            dict[remainder] = i

        remainder = num%den
        i=i+1

    return s if not neg else "-" + s

num=1
den=6
test=fractionToDecimal(num, den)
print(test)