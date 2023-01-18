'''This file calculates occurences of characters with and without dictionary'''

s = "I am learning python"

# using dict
freq = {}
for char in s:
    if char.isalpha():
        freq[char] = freq.get(char, 0) + 1
for char, val in freq.items():
    print(char + ":", val)

# without dict
'''
uniqueChars = ""
uniqueCharsFreq = 0
for char in s:
    if char.isalpha():
        pos = uniqueChars.find(char)
        if pos == -1:
            uniqueChars += char
            uniqueCharsFreq = uniqueCharsFreq * 10 + 1
        else:
            uniqueCharsFreq += (10 ** (len(uniqueChars) - pos - 1))
print(uniqueChars)
print(uniqueCharsFreq)
for n in range(len(uniqueChars) - 1, -1, -1):
    print(uniqueChars[n] + ':', uniqueCharsFreq % 10)
    uniqueCharsFreq //= 10
'''
