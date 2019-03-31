def convertToTitle(n):
    str = []
    i = 0

    while (n > 0):
        rem = n % 26
        if (rem == 0):
            str.append('Z')
            i = i + 1
            n = (n / 26) - 1
        else:
            str.append(chr((rem - 1) + ord('A')))
            i = i + 1
            n = n / 26

    str = str[::-1]
    return "".join(str)



test=convertToTitle(700)
print(test)