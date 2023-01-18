def testfunc1(a, b):
    return a + b


def testfunc2(a, b):
    return testfunc1(a, b)


def testfunc3():
    return 1,[],[]


def testfunc4(l):
    l.append(3)
    pass


print(testfunc1(10.1, 11))
print(type(testfunc3()))
l = [1,2]
testfunc4(l)
print(l)
