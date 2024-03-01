# Given 3 sides of a triangle, determine if it is a right triangle

## get user input


side1 = int(input("Enter side 1: "))
side2 = int(input("Enter side 2: "))
side3 = int(input("Enter side 3: "))

## find the longest side and set up pythag theorem checker
if (side1 > side2) & (side1 > side3) :
    c = side1
    b = side2
    a = side3

if (side2 > side1) & (side2 > side3) :
    c = side2
    b = side1
    a = side3

if (side3 > side1) & (side3 > side2) :
    c = side3
    b = side2
    a = side1
    
if (a**2+b**2==c**2) :
    print("This triangle has a right angle!")
else: 
    print("This triangle doesn’t have a right angle...")

