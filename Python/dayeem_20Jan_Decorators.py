# additional features to existing method

def secondDecorator(func):
    def inner(n1, n2):
        return func(n1, n2) * 3
    return inner


def myDecorator(func):
    def inner(n1, n2):
        n = 10
        f = func(n1, n2)
        return f + n
    return inner


@myDecorator
def func1(n1, n2):
    return n1 + n2


@secondDecorator
@myDecorator
def func2(n1, n2):
    return n1 + n2


n1, n2 = 20, 30
print(func1(n1, n2)) # 10 + (20 + 30)
print(func2(n1, n2)) # 3 * [10 + (20 + 30)]
