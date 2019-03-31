def run_length_encoding(str):
    dict={}
    size=len(str)
    for i in range(0,size):
        key=str[i]
        if(key not in dict):
            dict[key]=1
        else:
            dict[key]=dict[key]+1

    for key,value in dict.items():
        print(key,value)



str="SSMMMAAARRRRTTTT"
d=run_length_encoding(str)
print(d)


