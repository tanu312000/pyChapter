a=10

def f1():
    print(a)

def f2():
    print(a)


f1()
f2()

b=10

def f1():
    b=20
    print(b)

def f2():
    print(b)

f1()
f2()


b=10

def f1():
    global a
    a=20

    print(a)

def f2():
    print(a)

f1()
f2()

def f1():
    global a
    a=20
    print(a)

def f2():
    global a
    a=30
    print(a)

def f3():
    print(a)



f1()
f2()
f3()

a=10
def f1():
    global a
    a=111
    print(a)

def f2():
    print(a)

f1()
f2()