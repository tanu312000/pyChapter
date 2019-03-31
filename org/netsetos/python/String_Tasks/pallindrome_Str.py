import math
class pallindrome:
    def isPalindrome(self, A):
        import math
        A = ''.join(e for e in A if e.isalnum()).upper()
        n = len(A)

        for i in range(0, int(n / 2)):
            if (A[i] is not A[n - 1]):
                return 0
            return 1


dp=pallindrome()
str="A man, a plan, a canal: Panama"

p=dp.str_pallindrome(str)