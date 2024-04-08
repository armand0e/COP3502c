
from pakuri import Pakuri
from pakudex import Pakudex

def print_pakudex_menu():
    print("\nPakudex Main Menu")
    print("-----------------")
    print("1. List Pakuri")
    print("2. Show Pakuri")
    print("3. Add Pakuri")
    print("4. Evolve Pakuri")
    print("5. Sort Pakuri")
    print("6. Exit\n")


def main():
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    valid_input = False
    while not valid_input:
        capacity = input("Enter max capacity of the Pakudex: ")
        try:
            value = int(capacity)
            if value > 0:
                valid_input = True
            else:
                print("Please enter a valid size.")
                valid_input = False
        except ValueError:
            print("Please enter a valid size.")
            valid_input = False
    pakudex = Pakudex(capacity)
    print(f"The Pakudex can hold {capacity} species of Pakuri.")
    
    print_pakudex_menu()
    choice = input("What would you like to do? ")
    match choice:
        case 1:
            if pakudex.get_species_array() == None:
                print("No Pakuri in Pakudex yet!")
            else:
                lst = pakudex.get_species_array()
                print("Pakuri In Pakudex: ")
                for i in range(len(lst)):
                    print(f"{i+1}. {lst[i]}")
        case 2:
            pass
        case 3:
            pass
        case 4: 
            pass
        case 5:
            pass
        case 6:
            program_run = False


if __name__ == '__main__':
    main()
