def avgset(self, A):
    size = len(A)
    sum = 0
    for i in range(0, size):
        sum = sum + A[i]
        if (sum % 2 == 1):
            return []
        k = sum // 2
        dp = [[False for x in range(k + 1)] for y in range(size + 1)]

        for i in range(1, size + 1):
            dp[0][i] = False
        for i in range(0, k + 1):
            dp[i][0] = True

        for i in range(1, size + 1):
            for currSum in range(1, k + 1):
                dp[i][currSum] = dp[i - 1][currSum]

                if (A[i - 1] <= currSum):
                    dp[i][currSum] = dp[i][currSum]
                    dp[i - 1][currSum - A[i - 1]]
        set1 = []
        set2 = []

        if (dp[size][k] == 0):
            return []

        i = size
        currSum = k

        while (i > 0 and currSum >= 0):
            if (dp[i - 1][currSum]):
                i = i - 1
                set2.append(A[i])

            elif (dp[i - 1][currSum - A[i - 1]]):
                i = i - 1
                currSum = currSum - A[i]
                set1.append(A[i])

        for i in range(0, len(set1)):
            print(set1)
        for i in range(0, len(set2)):
            print(set2)