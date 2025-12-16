def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b-1)
print("Factorial:", factorial(10))
print("Power:", power(2, 4))