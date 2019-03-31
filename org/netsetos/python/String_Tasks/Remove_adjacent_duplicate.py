def remove_duplicate(str,len):
    k=0
    i=1
    while(i<len-1):
        if(str[i-1] != str[i]):
            str[k]=str[i-1]
            k = k + 1

        else:
            while(str[i-1] == str[i]):
                i=i+1
        i=i+1

    str[k]=str[i-1]
    k = k + 1

    #str[k]="\0"

    str=str[0:k]
    print(str,k)
    if(k!=len):
        return remove_duplicate(str,k)

    return str

print(remove_duplicate(['r','a','v','i','n','n','n','i','v','a'],10))
