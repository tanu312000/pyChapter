class max_sliding_element:
    def sliding_Element(arr,slide):
        size=len(arr)

        for i in range(size-slide+1):
            max=arr[i]

            for j in range(1,slide):
                if(arr[i+j]>max):
                    max=arr[i+j]
            print(max)

    arr = [10,4,2,11,3]
    data = sliding_Element(arr)
    print(data)