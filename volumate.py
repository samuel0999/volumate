# VoluMate
import math

def calculate_the_volume():
    print("Calculate the Volume")
    print("selection of bodies")
    print("1. Cube")
    print("2. Block")
    print("3. Cylinder")
    print("4. Cone")
    print("5. Ball")


choice_body = input("Enter which body you want to use:")

if choice_body == "1":
    a = float(input("Enter side A:"))
    volume = a ** 3
    print(f"The volume of cube is: {volume:.2f}")
elif choice_body == "2":
    a = float(input("Enter side A:"))
    b = float(input("Enter side B:"))
    c = float(input("Enter side C:"))

    volume = a * b * c

    print(f"The volume of block is: {volume:.2f}")
elif choice_body == "3":
    r = float(input("Enter radius or r:"))
    v = float(input("Enter high v:"))

    volume = math.pi * r**2 * v
    print(f"The volume of cylinder is: {volume:.2f}")
elif choice_body == "4":
    r = float(input("Enter radius or r:"))
    v = float(input("Enter high v:"))

    volume = (1/3) * math.pi * r**2 * v
    print(f"The volume of cone is: {volume:.2f}")

elif choice_body == "5":
    r = float(input("Enter radius ball r:"))
    volume = (4/3) * math.pi * r**3
    print(f"The volume of ball is: {volume:.2f}")
else:
    print("Invalid input!\n")

calculate_the_volume()