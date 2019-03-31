from bisect import bisect_right as upper_bound

def findMedian(A):
    R = len(A)
    C = len(A[0])
    mi = A[0][0]
    mx = 0
    for i in range(R):
        if (A[i][0] < mi):
            mi = A[i][0]
        if (A[i][C - 1] > mx):
            mx = A[i][C - 1]

    desired = (R * C + 1) / 2
    while(mi < mx):
        mid = mi + (mx - mi) // 2
        place = [0]

        for i in range(R):
            j = upper_bound(A[i], mid)
            place[0] = place[0] + j
        if (place[0] < desired):
            mi = mid + 1
        else:
            mx = mid
    return mi


arr=[[1, 3, 5],[2, 6, 9],[3, 6, 9]]
p= findMedian(arr)
print(p)
