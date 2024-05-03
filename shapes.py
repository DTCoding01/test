import math

length = int(input("What is the length of your rectangle? "))
width = int(input("What is the width of your rectangle? "))

print(f"The rectangle has the area: {length * width}")

radius = int(input("What is the radius of your circle? "))

print(f"The area of your circle is: {(radius ** 2) * math.pi}")

base = int(input("What is the base of your triangle? "))
height = int(input("What is the height of your triangle? "))

print(f"The triangle has the area: {(base * height) / 2}")