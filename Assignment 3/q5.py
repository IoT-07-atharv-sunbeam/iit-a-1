def greet(name="User"):
    print("Hello", name)
def add(a, b):
    return a + b
def apply(a, b, func):
    return func(a, b)
greet()
greet("Atharv")
print(apply(10, 20, add))