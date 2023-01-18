s = 'I am learning Python'
print('Slice:', s[5:10])
print('Reverse:', s[::-1])
print('Reverse from end to index 4: ', s[:3:-1])
print('Split string on space:', s.split(" "))
print('First occurence of "Py":', s.find('Py', 0, len(s)))
#index as well but throws error when not found
print('Converting list to str:', " ".join(s.split(" ")))
