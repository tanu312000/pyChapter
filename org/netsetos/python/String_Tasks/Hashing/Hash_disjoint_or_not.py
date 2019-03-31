def Hash_disjoint_or_not(arr1,arr2):
    dict={}
    size1=len(arr1)
    size2=len(arr2)
    for i in range(0,size1):
        dict[arr1[i]]='inserted'
    print(dict)

    for i in range(0,size2):
        if(arr2[i] in dict):
            print("Not Disjoint")

arr1=[1,2,4,5,6,11]
arr2=[12,24,16,17,18]
Hash_disjoint_or_not(arr1,arr2)
