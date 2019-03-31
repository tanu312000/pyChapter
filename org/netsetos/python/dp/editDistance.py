def EditDistanceDP(str1,str2,len1,len2):
    dp=[[0 for x in range(len2+1)]for x in range(len1+1)]

    for i in range(len1+1):
        for j in range(len2+1):
            if(i==0):
                dp[i][j]=j

            elif(j==0):
                dp[i][j]=i

            elif(str1[i-1]==str2[j-1]):
                dp[i][j]=dp[i-1][j-1]

            else:
                dp[i][j]=1+min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])

    return dp[len1][len2]


str1="SATURDAY"
str2="SUNDAY"

print(EditDistanceDP(str1, str2, len(str1), len(str2)))