class Solution:

    # def ExcelCol_num(name):
    #     pow=1
    #     colNum=0
    #     for letter in name[::-1]:
    #         colNum +=(int(letter,36)-9)*pow
    #         pow=pow*26
    #     return colNum

    # def colnum_string(n):
    #     string = ""
    #     while n > 0:
    #         n,remainder = divmod(n - 1, 26)
    #         string = chr(65 + remainder) + string
    #
    #     print(string)


    #colnum_string(1)

    def printString(A):
        MAX=50
        string = ["\0"] * MAX


        i = 0

        while (A > 0):
            # Find remainder
            rem = A % 26

        # if remainder is 0, then a
        # 'Z' must be there in output
            if rem == 0:
                string[i] = 'Z'
                i += 1
                A = (A / 26) - 1
            else:
                string[i] = chr((rem - 1) + ord('A'))
                i += 1
                A = A / 26
        string[i] = '\0'

    # Reverse the string and print result
        string = string[::-1]
        print( "".join(string))

# Driver program to test the above Function
    printString(14)





