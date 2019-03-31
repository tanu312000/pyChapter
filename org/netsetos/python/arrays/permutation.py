def permutation_helper(self,arr,output,start,end):

    if(start==end):
        output.append(arr[:])
    else:
        for index in range(start,end):
            arr[start],arr[index]=arr[index],arr[start]
            permutation_helper(arr,output,start+1,end)
            arr[start], arr[index] = arr[index], arr[start]

