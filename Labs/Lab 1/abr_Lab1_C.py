# You are given two lines in slope-intercept form (y = mx + b) and must find their intersection point
# Develop a program to find the intersection of any two lines 

## take inputs
m1 = float(input("Enter m for Line 1: "))
b1 = float(input("Enter b for Line 1: "))

m2 = float(input("Enter m for Line 2: "))
b2 = float(input("Enter b for Line 2: "))

## manipulate variables
### m1(x) + b1 = m2(x) + b2 then (m1- m2)x = b2-b1

x = (b2 - b1) / (m1 - m2)
y = (m1 * x) + b1

## program output
print(f"The intersection point is ({round(x, 2)},{round(y, 2)})")

