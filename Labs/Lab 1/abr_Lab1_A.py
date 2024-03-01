# Program start

## explain program to user
# print("The purpose of this program is to calculate the equivalent resistance (R) of three resistors in parallel")

## gather user inputs and store them into variables r1, r2, r3
r1 = float(input("What is the value of R1? "))
r2 = float(input("What is the value of R2? "))
r3 = float(input("What is the value of R3? "))

## mainpulate variables
r = 1/((1/r1)+(1/r2)+(1/r3))

## print desired output(s)
print(f"The equivalent resistance is {r} ohms")
