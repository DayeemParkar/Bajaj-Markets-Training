from functools import reduce

X = lambda x, y:x + y
print(X(10,20))
L = [1,2,3,4]
L = list(map(lambda x:x**3, L))
print(L)
L1 = list(filter(lambda x:x%3==0, L))
print(L1)
L2 = reduce(lambda x, y: x + y, L)
print(L2)
