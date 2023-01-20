# yield - keep track of last

# return 1, come back, return 2, come back and so on
def count(n):
    i = 1
    while i <= n:
        yield i
        i += 1


class MyIterator:
    def __init__(self, l, h):
        self.l = l
        self.h = h
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.l <= self.h:
            self.l += 1
            return self.l - 1
        else:
            raise StopIteration


g = count(10)
print(type(g))
print(g)
for i in g:
    print(i)
    if i == 10:
        break

print('My Iteration')
it = MyIterator(20, 30)
for i in it:
    print(i)
