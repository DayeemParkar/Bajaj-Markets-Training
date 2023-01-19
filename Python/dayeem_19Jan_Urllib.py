from urllib.request import urlopen
import csv

url = r'https://raw.githubusercontent.com/tokern/piicatcher/master/tests/samples/sample-data.csv'

def read_data(u):
    if u.startswith(('https:', 'http:', 'ftp:')):
        return urlopen(url).read()
    return

s = read_data(url).decode('utf-8')
if not s:
    print('Something went wrong')
else:
    rows = s.split('\r\n')
    data = []
    for row in rows:
        cols = row.split(',')
        if len(cols) == 16:
            data.append(cols[0]+','+cols[1]+','+cols[2]+','+cols[4]+','+cols[5])

with open('somedata.csv', 'w') as f: 
    for line in data:
        f.write(line + '\n')
f.close()
