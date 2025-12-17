from geometry import area_circle, area_rectangle

r = float(input("Enter radius of circle: "))
l = float(input("Enter length of rectangle: "))
w = float(input("Enter width of rectangle: "))

print("Area of circle:", area_circle(r))
print("Area of rectangle:", area_rectangle(l, w))
