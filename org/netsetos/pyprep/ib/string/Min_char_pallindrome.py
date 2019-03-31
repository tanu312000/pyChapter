def solve(self, A):
    res = self.min_char_pallin(A, 0, len(A) - 1)
    return res


def min_char_pallin(self, str1, start, end):
    if (start > end):
        return sys.max
    elif (start == end):
        return 0
    elif (start == end - 1):
        if (str1[start] == str1[end]):
            return 0
        return 1

    if (str1[start] == str1[end]):
        return self.min_char_pallin(str1, start + 1, end - 1)
    else:
        return (min(self.min_char_pallin(str1, start, end - 1),
                    self.min_char_pallin(str1, start + 1, end)) + 1)