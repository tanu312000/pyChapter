def minWindow(S, T):
    from collections import defaultdict
    count_dict = defaultdict(int)

    for c in T:
        count_dict[c] += 1

    st = 0
    end = 0
    remaining = len(T)
    min_st = 0
    min_len = len(S) + 1

    n = len(S)
    while end < n:
        if count_dict[S[end]] > 0:
            remaining -= 1

        count_dict[S[end]] -= 1
        end += 1

        while remaining == 0:
            if end - st < min_len:
                min_len = end - st
                min_st = st

            count_dict[S[st]] += 1
            if count_dict[S[st]] > 0:
                remaining += 1
            st += 1

    if min_len == len(S) + 1:
        return ""

    return S[min_st:min_st + min_len]

A="ADOBECODEBANC"
B="ABC"
test=minWindow(A,B)
print(test)
