class combine:
    def letterCombinations(self, A):
        length = len(A)
        currNum = 0
        digit = A
        phone = {1: ["1"], 2: ["a", "b", "c"], 3: ["d", "e", "f"], 4: ["g", "h", "i"], 5: ["j", "k", "l"],
                 6: ["m", "n", "o"], 7: ["p", "q", "r", "s"], 8: ["t", "u", "v"], 9: ["w", "x", "y", "z"], 0: ["0"]}
        currString = ""
        answer = []
        self.util_func(answer, phone, digit, currNum, currString, length)
        return answer


    def util_func(self, answer, phone, digit, currNum, currString, length):
        if (currNum == length):
            answer.append(currString)
            return
        for i in range(0, len(phone[int(digit[currNum])])):
            t1 = phone[int(digit[currNum])]
            currString = currString + t1[i]

            self.util_func(answer, phone, digit, currNum + 1, currString, length)
        return

sc=combine()
A="23"





d=sc.letterCombinations(A)
print(d)


