try:
    f=open('/home/tanu/Desktop/integer.txt')
    s=f.readline()
    i=int(s.strip())
except (IOError,ValueError as e):

    print("Expected Error Occurred")
except:
    print("Unexpected Error occurred")
finally:
    print("Bye")


