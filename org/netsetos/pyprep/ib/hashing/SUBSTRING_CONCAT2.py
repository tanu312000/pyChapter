def substring_indices(S,L):
    from collections import defaultdict
    hashmap = defaultdict(int)
    temp_hashmap = defaultdict(int)
    size_word = len(L[0])
    # Number of words present inside list L.
    word_count = len(L)
    # Total characters present in list L.
    size_L = size_word * word_count
    res=[]
    if (size_L > len(S)):
        return res
    #Map stores the words present in list L
    # hashmap={}
    i=0
    for i in range(0,word_count):
        hashmap[L[i]]+=1

    for i in range(0,len(S)-size_L+1):
        # temp_hashmap={}
        j=i
        #Traverse the substring
        while (j < i + size_L):
            word = S[j:size_word]
            #If word not found simply
            if (word not in hashmap):
                break
            else:
                temp_hashmap[word]-=1

            j += size_word
        count = 0
        for key in temp_hashmap.keys():
            if(temp_hashmap[key]>0):
                count=count+1
        if(count==0):
            res.append(i)
    return res

S="barfoothebarfooman"
L=["foo","bar"]
test=substring_indices(S,L)
print(test)