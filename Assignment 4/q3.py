def overlapping(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False


list1 = list(map(int, input("Enter elements of first list separated by space: ").split()))
list2 = list(map(int, input("Enter elements of second list separated by space: ").split()))

result = overlapping(list1, list2)

print("Overlapping:", result)