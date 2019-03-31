def generate_all_numeral(currentNum,symbol,symVal):
    count=0
    while(currentNum >=symVal):
        currentNum = currentNum - symVal
        count=count+1
        romancount=symbol*count
    return romancount

print("This program converts any number to Roman Number")

n=input("Enter a number")

def to_roman(n):
    M=generate_all_numeral(n,'M',1000)
    n=n-(count*1000)
    CM = generate_all_numeral(n, 'CM', 900)
    n = n - (count * 900)
    D = generate_all_numeral(n, 'D', 500)
    n = n - (count * 500)
    CD = generate_all_numeral(n, 'CD', 400)
    n = n - (count * 400)
    C = generate_all_numeral(n, 'C', 100)
    n = n - (count * 100)
    L = generate_all_numeral(n, 'CM', 50)
    n = n - (count * 50)
    XLV = generate_all_numeral(n, 'XLV', 45)
    n = n - (count * 45)
    XL = generate_all_numeral(n, 'XL', 40)
    n = n - (count * 40)
    X = generate_all_numeral(n, 'X', 10)
    n = n - (count * 10)
    IX = generate_all_numeral(n, 'IX', 10)
    n = n - (count * 9)
    V = generate_all_numeral(n, 'V', 5)
    n = n - (count * 5)
    IV = generate_all_numeral(n, 'IV', 4)
    n = n - (count * 4)
    I = generate_all_numeral(n, 'I', 1)
    n = n - (count * 1)
    return M+CM+D+CD+C+L+XLV+XL+X+IX+V+IV+I
