import functools
def Largest_Number(num):
    def compare(n1,n2):
        if(n1+n2 >n2+n1):
            return 1
        elif (n1 + n2 < n2 + n1):
            return -1
        else:
            return 0

    num_str = [str(n) for n in num]
    res = ""

# Sorting according to customized function
    for n in reversed(sorted(num_str, key=functools.cmp_to_key(compare))):
        res += n

#Remove unncessary zero in head
    res_list = list(res)
    i = 0
    while (res_list[i] == '0' and i != len(res) - 1):
        i += 1
    res_list = res_list[i:]

    return ''.join(res_list)

num=[3,30,34,5,9]
d=Largest_Number(num)
print(d)