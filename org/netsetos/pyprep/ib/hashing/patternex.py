def pattern234(str,pat):
    size1=len(str)
    size2=len(pat)

    for index1 in range(0,size1-size2+1):
        index2=0
        for index2 in range(0,size2):
            if(str[index1+index2]!=pat[index2]):
                break
        if(index2==size2-1):
            print("Pattern found",index1)

text="foobarthefoobarman"
pattern="foobar"
pattern234(text,pattern)
