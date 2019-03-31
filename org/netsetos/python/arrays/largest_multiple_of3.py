class largest:
    def findmaxmultipleof3(self,arr,size):
        for j in range(1, len(arr)):
            i = j - 1
            key = arr[j]
            while (i >= 0 and key < arr[i]):
                arr[i + 1] = arr[i]
                i = i - 1
            arr[i + 1] = key
        for i in range(size):
            sum=0
            q0,q1,q2
            sum=sum+arr[i]
            if(arr[i]%3==0):
                arr[i].append(q0)
            elif(arr[i]%3==1):
                arr[i].append(q1)
            else:
                arr[i].append(q2)

        if(sum%3==1):
