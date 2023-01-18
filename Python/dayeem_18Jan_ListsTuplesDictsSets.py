print('Lists:')
l = [3,7,2,9]
l.append(11)
l.sort(reverse=True)
print(l)
l.append((1,2,3))
print(l)
l.extend((4,5,6))
print(l)
l.insert(4, 500)
print(l)
l.pop()
print(l)
l.remove(4)
print(l)
del l[0]
print(l)
l.clear()
print(l)

print('\nTuples:')
t = (1,3,4)
print(t.count(3))
print(t.index(4))

print('\nDictionaries:')
# key can be str, number, tuples without mutable objs in it
d = {1:'one'}
d[2] = 'and'
print(d.get(2))
print(d.get(3, 'Nothing found'))
print(sorted(d))
print(sorted(d.values()))
l = [1,2,3]
d = d.fromkeys(l, 0)
print(d)
l1 = ['Ind', 'Chi', 'Sri']
l2 = ['Pune', 'Beijing', 'Kolambo']
d = dict(list(zip(l1, l2)))
print(d)

print('\nSets:')
s1 = {1,2,3,6,7,8}
s2 = {1,2,10,11,3,8}
s1.add(10)
s1.remove(2)
print('s1:', s1)
print('S2:', s2)
print(s1.union(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))
print(s1.intersection(s2))
