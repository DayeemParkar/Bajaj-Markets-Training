# try except finally

class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg


def check(d):
    for k,v in d.items():
        print(k, v)
        if v < 2000:
            raise CustomException('Low Balance')


def avg(L):
    t = 0
    for i in L:
        t += i
    return t, t / len(L)


b = {'Raj':4000, 'Dev':1500, 'Mahesh':1000}
try:
    check(b)
except CustomException as cust:
    print(cust)

try:
    name = input('Filename: ')
    f = open(name, 'r')
except IOError as ie:
    print('File not found')
else:
    print('File has', len(f.readlines()), 'lines')
    f.close()

try:
    t, a = avg([1,2,3,4,'p'])
    print('Total is', t, 'and avg is', a)
except TypeError as te:
    print(te)
except ZeroDivisionError as ze:
    print(ze)

try:
    f = open('myfile', 'r')
    a, b = [int(x) for x in input('Two nos: ').split()]
    c = a / b
    f.write('Write into file' % c)
    f.close()
except ZeroDivisionError as ze:
    print('Error:', ze)
