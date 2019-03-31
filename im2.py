import sys
a=10
b=0
try:
    c=a/b
    print(c)
except ValueError as e:
    print(e)

except:
    print(f'Unknown Error: {sys.exc_info()}')

else:
    print("Good Job")

# print("Hello")
# print(10/0)
# print("Hi")

try:
	print("try")
	print(10/0)
except ZeroDivisionError:
	print("except")
finally:
	print("finally")


try:
	print("try")
	print(10/0)
except NameError:
	print("except")
finally:
	print("finally")

import os

try:
	print("try")
	os._exit(0)
except ZeroDivisionError:
	print("except")
finally:
	print("finally")
