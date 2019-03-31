def lastword(A):
    A=A.rstrip(' ')
    new_word=A.split(' ')
    no_of_words=len(new_word)
    if(no_of_words ==1):
        return len(A)
    else:
        last_word=new_word[-1]
        return len(last_word)

A='Hello Sarthak'
test=lastword(A)
print(test)
