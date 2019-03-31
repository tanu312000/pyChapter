class Solution:

    def combinationSum(self, A, B):
        candidates = A
        target = B
        temparr = []

        for i in A:
            if (i not in temparr):
                temparr.append(i)
        temparr.sort()
        candidates = temparr
        combinations = []
        curr = []

        self.helper(candidates, target, curr, combinations, 0)

        return combinations


    def helper(self, candidates, target, curr, combinations, index):
        if (target <= 0):
            if (target == 0):
                combinations.append(list(curr))
            return

        if (index < len(candidates) ):
            value = candidates[index]
            curr.append(value)
            self.helper(candidates, target - value, curr, combinations, index+1)
            curr.pop()
            self.helper(candidates, target, curr, combinations, index + 1)

    def combinationSum2(self, A, B):

        def combUtil(cur, rest, target, res):
            if target < 0:
                return
            if target == 0:

                if len(res) == 0 or cur != res[-1]:
                    res.append(cur[:])
                return
            if len(rest) == 0:
                return
            cur.append(rest[0])
            combUtil(cur, rest[1:], target - rest[0], res)
            cur.pop()
            combUtil(cur, rest[1:], target, res)

        res = []
        combUtil([], sorted(A), B, res)
        return res


sd=Solution()
arr=[2,3,5 ]
target=8
er=sd.combinationSum2(arr,target)
print(er)