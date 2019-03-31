def substring1(A):
    n=len(A)
    dict=set()
    dict.add("A")
    dict.add("a")
    dict.add("e")
    dict.add("E")
    dict.add("i")
    dict.add("I")
    dict.add("o")
    dict.add("O")
    dict.add("u")
    dict.add("U")

    for i in range(0, n):
        for j in range(i, n + 1):
            if(A[i:j].startswith("A") or A[i:j].startswith("E") or
            A[i:j].startswith("I") or A[i:j].startswith("O") or
            A[i:j].startswith("U")):
                print(A[i:j])


A="xIOPYCHpQNLyIdeFIYVojbccFLnWrJcwougkVYUTXvSWLXPEMjoIXWDLJnslpMVEyrLWFvNvteWgfTvTUboqaPEUCuldrbHAPpyvEMjUKslmCmZHDEsnhhcwgzvBNtabMWHykYsOAUHAaDMcuXMyqtXHpVVRydXcmJVCjrSITpFydNDGOVrJDWYcJcVaWdoshbaPXAFOtgtCvtqeGlaYoycQQJrcGseoYEPBqrCrKdRMelddPFguYcVIPdzKEBtycORccDtxUhgeffNJjCINqJGqbxvFmJUxNzhyZdHKwshMqVjUxKEEtvfaxDfwpfyUqHmVIDabhcnCSqDnegyKMlBCvVMRhSwDlZCaSRyjnJKKCEEJQlIcFucFGoKvNPAnruCSkCFAFLGvQfHyxkRjGzBcznEUBmfypnBqEqvBDrBlDMxCXSjnhxsYLcVxEPgetYVHFRsGmblhecIADMLtZodelDyFoplSbgRCwZgUvrSKMartSZlhzaywoIgKALNyLdIZlmgTqTRQAcbUTsbXddQYToZPFMrATjfWJrlNtSngZqEBIAprYlOoarTvJShGtxFKOIeowFlJetauEREhKGzeuXKmlvXRonMuMSowznjKWcelUuLcEAwLsIHZQmEozdVQGRrUQtUpzYembyhopxNMjpHSPEXOwHfNhRnveBZEtwfnpCZrdFafrzWFfKKofcLueRRFtZSuadasEfyGQnzMYxbhUrIycauVINDOeXMGQgWIhXdSIpuNFHAvIBmUjOUmdBZPlCWDOqBakqQeNWHCNEJgynYfJdMYlsjhbNSUaPExSIQefRYeLOXfWtprBBqbBlHIcfspzmqcpGwrXQbqJvtOJUdbIKBxVuZFKKSzjZBuEFakcWuAodBegkyCEahrWWeGACCmjkzryEIAnSOZPYmAMuDkNSuSmDTZPrzFnypKjwmIknMHvPsnkDnXXDVtqycaTClMFxLnZRnuEjotvjKQMzXwdMqugMLQ"
test=substring1(A)
