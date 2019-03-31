def maxPoints(A, B):
    if len(A) == 1: return 1
    # print A, B
    finalMax = 0

    for i in range(len(A) - 1):
        slopes = {}
        slopeCount = 0
        same_count = 0
        verticalCount = 0
        x1, y1 = A[i], B[i]
        for j in range(i + 1, len(A)):
            if i != j:
                x2, y2 = A[j], B[j]
                if x1 == x2 and y1 == y2:
                    same_count += 1
                elif x1 == x2:
                    verticalCount += 1
                    slopeCount = max(slopeCount, verticalCount)
                else:
                    slope = ((y2 - y1) * 1.0 / (x2 - x1))
                    if slope not in slopes:
                        slopes[slope] = 1
                        slopeCount = max(slopeCount, slopes[slope])
                    else:
                        slopes[slope] += 1
                        # print i,j, slopes[slope], slope, y2, y1
                        slopeCount = max(slopeCount, slopes[slope])

        finalMax = max(slopeCount + same_count + 1, finalMax)

    return finalMax
A=
maxPoints(A, B)

# if(k==len(s)):
#     result.append(curr_result)
#     return
#
# for i in range(k+1,len(s)+1):
#     if(self.ispallin(s[k:i])):
#         curr_result.append(s[k:i])
#         self.helper(result,curr_result,s,i)
#         curr_result.pop()
