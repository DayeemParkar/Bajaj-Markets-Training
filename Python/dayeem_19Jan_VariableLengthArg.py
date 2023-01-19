import pdb

pdb.set_trace()

def myFunc(*args, **kwargs):
    print(type(args), type(kwargs))
    print(args, kwargs)

myFunc(1,2,5)
myFunc(1,'random', 15.2)
