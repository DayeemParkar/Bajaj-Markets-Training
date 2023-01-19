import re

# emails
f = open('findEmails.txt', 'r')
lines = f.readlines()
for line in lines:
    if re.match(r'^\w+@\w+(\.\w+)*$', line):
        print(line)
f.close()

# dates
s = 'Today is 19/01/2023. Next class will be from 6/10/2023'
dates = re.findall(r'[0-9]{1,2}/[0-9]{1,2}/[0-2][0-9]{3}', s)
print(dates)
