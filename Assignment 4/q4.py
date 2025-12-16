def histogram(numbers):
    for num in numbers:
        print(f"{num}: " + "*" * num)


values = list(map(int, input("Enter integers separated by space: ").split()))

histogram(values)