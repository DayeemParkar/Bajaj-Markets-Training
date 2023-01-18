def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

def reverse(s):
    if len(s) == 0:
        return ""
    return s[-1] + reverse(s[:len(s) - 1])

print(factorial(10))
print(reverse('Shivam'))