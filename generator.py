def my_gen():
    n=1
    print("This is printing 1st")
    yield n

    n+=1
    print("This is printing 2nd")
    yield n

    n+=1
    print("This is printing 3rd")
    yield n


for item in my_gen():
    print(item)
# print(next(a))
# print(next(a))
# next(a)
# next(a)
# next(a)
