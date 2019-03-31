try:
    print(10//0)
    print(int(input()))

except ZeroDivisionError as e:
    print("Exception Caught",e)
except ValueError:
    print("Exception Caught", e)
print("the end")

a=10
b=0

try:
    c=a/b
    print(c)
except:
    print("Exception Caught")

finally:
    print("clean up operations")
print("byee")

while True:
    try:
        n = input("Please enter an integer: ")
        n=int(n)
        break

    except ValueError:
        print("No valid integer! Please try again...")

print("Great! you successfully installed")




try:
    f = open('/home/tanu/Desktop/integer.txt')
    s = f.readline()
    i = int(s.strip())

except IOError as e:
    print(e)
except ValueError:
    print("No Valid Integer")
except:
    print("Unexpected Error:")
finally:
    f.close()