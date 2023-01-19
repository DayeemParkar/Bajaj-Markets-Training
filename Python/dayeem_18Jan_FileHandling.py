'''This file creates a new file with some data 
and then edits that data using a temp file as an intermediate'''

import os

# modes - w, wt, r, rt, a, at, wb, rb
f = open("test.txt", "w")
f.write('Line 1\n')
f.write('Line 2\n')
f.write('Line 3\n')
f.write('Line 4\n')
f.write('Line 5\n')
f.write('Line 6\n')
f.write('Line 7\n')
f.write('Line 8\n')
f.write('Line 9\n')
f.write('Line 10')
f.close()

with open('test.txt', 'r') as f:
    lines = f.readlines()
    lines[4] = 'Line 5 edited\n'
    lines[5] = 'Line 6 edited\n'

    f1 = open('temp.txt', 'w')
    f1.writelines(lines)
    f1.close()
f.close()

os.remove('test.txt')
os.rename('temp.txt', 'test.txt')

'''
os.chdir(os.getcwd() + '/__pycache__')
print(os.getcwd())
'''
