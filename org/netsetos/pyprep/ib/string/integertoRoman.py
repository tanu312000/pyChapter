
def intToRoman(A):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    res = ""
    i=0
    while(A>0):
        if(A-values[i]>=0):
            res=res+(numerals[i])
            A =A-values[i]
        else:
            i=i+1
    return res

test=intToRoman(39)
print(test)