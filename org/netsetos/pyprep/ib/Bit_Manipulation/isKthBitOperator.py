def KthBitOpera(n,k):
    temp=1
    temp<<(k-1)

    if(n&temp >0):
        print("Set")
    else:
        print("Not a Set")




d=KthBitOpera(5,3)
