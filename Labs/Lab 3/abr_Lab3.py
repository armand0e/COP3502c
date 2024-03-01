import math

def menu(result):
    print (f"\nCurrent Result: {result}\n")
    print("Calculator Menu\n---------------\n0. Exit Program\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponentiation\n6. Logarithm\n7. Display Average")

program_run = True
calculations = 0
print_menu = True
result = 0.0
calculation_sum = 0.0
while program_run:
    if print_menu == True:                                          # print menu
        menu(result)
    selection = int(input("Enter Menu Selection: "))                # ask for menu selection
    if selection == 0:                                              # option 0 exit program
        print("Thanks for using this calculator. Goodbye!")
        program_run = False
        
    elif selection <= 6 and 1 <= selection:                         # options 1-6
        num1 = float(input("Enter first operand: "))
        num2 = float(input("Enter second operand: "))
        match selection:
            case 1:                                                 # addition
                result = num1 + num2
            case 2:                                                 # subtraction
                result = num1 - num2
            case 3:                                                 # multiplication
                result = num1 * num2
            case 4:                                                 # division
                result = num1 / num2
            case 5:                                                 # exponent
                result = num1 ** num2
            case 6:                                                 # logarithm
                result = math.log(num2,num1)
        calculation_sum += result
        calculations += 1
        print_menu = True                                           ## everything here results in a new menu print
        
    elif selection == 7:                                            # option 7 display average
        if calculations == 0:
            print("Error: No calculations yet to average!\n")
        else:
            print(f"Sum of calculations: {calculation_sum}")
            print(f"Number of calculations: {calculations}")
            print(f"Average of calculations: {round(calculation_sum/calculations,2)}")
        print_menu = False                                          ## everything here results in no new menu print
            
    else: 
        print("Error: Invalid selection!")
        print_menu = False