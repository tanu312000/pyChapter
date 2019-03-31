import collections
def Min_window_substring(s,t):
    need=collections.Counter(t)
    l=0
    r=0
    i=0
    j=0
    missing=len(t)
    while(r<len(s)):
        print(need)
        if(need[s[r]] > 0):
            missing=missing-1
            need[s[r]]=need[s[r]]-1
        r=r+1
        while(missing==0):
            if(j==0 or r-l <j-i):
                i,j=l,r
            print(s[l])
            need[s[l]] = need[s[l]] + 1
            if(need[s[l]]>0):
                missing=missing+1
            l=l+1
    return s[i:j]


print(Min_window_substring("acbdnracbn",'abn'))