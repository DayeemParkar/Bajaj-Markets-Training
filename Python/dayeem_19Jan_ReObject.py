import re

# \w denotes A-Z,a-z,0-9
p = re.compile(r'm\w\w')
s = 'Cat Rat mat Sat men'

r = p.search(s)
r2 = p.findall(s)
# group return the matched section
print(r.span(), r.group())
print(r2)
print()

s = 'This; is the: "core" Python'
# \W means not \w, + means 1 or more
r = re.split(r'\W+', s)
print(r)
print()

s = 'This is beautiful'
r = re.sub(r'beautiful', r'ugly', s)
print(r)
print()

s = 'an apple a day keeps the doctor away'
r = re.findall(r'a[\w]*', s)
print(r)
print()

s = 'one two three four five six seven 8 9 10'
r = re.findall(r'\b\w{3,5}\b', s)
print(r)
r = re.findall(r'\b\d\b', s)
print(r)
print()

s = 'one two three one two three'
r = re.findall(r't[\w]*$', s)
print(r)
