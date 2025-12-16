def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return "error" if b == 0 else a / b
while True:
    print("1.add 2.sub 3.Multi 4.Div 5.exit")
    ch = int(input("Enter choice: "))
    if ch == 5:
        break
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    if ch == 1: print(add(a, b))
    elif ch == 2: print(sub(a, b))
    elif ch == 3: print(mul(a, b))
    elif ch == 4: print(div(a, b))