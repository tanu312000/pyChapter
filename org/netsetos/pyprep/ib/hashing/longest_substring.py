def longest_substring(str):
    start=0
    end=0
    max1=0
    set1=set()
    for end in range(0,len(str)):
        if(str[end] in set1):
            while(str[start]!=str[end]):
                set1.remove(str[start])
                start=start+1
            set1.remove(str[start])
            start = start + 1
        set1.add(str[end])
        max1=max(max1,len(set1))
    return max1

str="bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
d=longest_substring(str)
print(d)