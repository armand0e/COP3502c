# For a given length and width of a rectangle,
# write a program to calculate and display the perimeter, area and the length of the diagonal of the rectangle.

#take user input
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

# mainpulate variables
perimeter = (2*length) + (2*width)
area = length * width
diagonal = (length**2 + width**2)**(1/2)

# program output
print(f"Rectangle perimeter: {round(perimeter, 2)}")
print(f"Rectangle area: {round(area, 2)}")
print(f"Rectangle diagonal: {round(diagonal, 2)}")