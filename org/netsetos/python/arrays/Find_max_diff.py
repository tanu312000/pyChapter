#find max difference b/w
class FindMaxDiff:
    def find_max(arr):
        curr_max=0
        size=len(arr)
        for i in range(size):
            for j in range(i+1,size):
                diff=arr[j]-arr[i]
                if(diff > curr_max):
                    curr_max=diff
        print(j,i,curr_max)

        return curr_max

    def find_max_so_far(arr):
        min_ele_so_far=arr[0]
        max_diff_so_far=arr[1]-arr[0]
        curr_diff = arr[1] - arr[0]
        size=len(arr)
        for index in range(1,size):
            if(arr[index]<min_ele_so_far):
                min_ele_so_far=arr[index]
            else:
                curr_diff=arr[index]-min_ele_so_far
                if(curr_diff>max_diff_so_far):
                    max_diff_so_far=curr_diff
        print(max_diff_so_far)
        return max_diff_so_far

    def find_maxdiff_sum_subarray(arr):

        size=len(arr)
        diff={}
        for i in range(0,size-1):              #create difference array
            diff[i]=arr[i+1]-arr[i]

        max_diff=diff[0]
        for i in range(1,size-1):
            if(diff[i-1]>0):
                diff[i]=diff[i]+diff[i-1]

            if(max_diff < diff[i]):
                max_diff=diff[i]

        return max_diff



    arr =[1,10]
    data=find_max_so_far(arr)

    print(data)


