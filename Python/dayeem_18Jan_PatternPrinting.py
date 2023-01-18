'''This file prints a pattern of astericks and alphabets'''

n = 7
for a in range(n):
    print (" " * (n - a - 1) + "* " * a)

alpha = 65
print()
for a in range(n):
    print (" " * (n - a - 1), end="")
    for b in range(a + 1):
        print(chr(alpha), end=" ")
        alpha = min(alpha + 1, 90)
    print()
