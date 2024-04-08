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
    # welcome
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    # get capacity
    valid_capacity = False
    while not valid_capacity:
        capacity = input("Enter max capacity of the Pakudex: ")
        # check validity
        try:
            capacity = int(capacity)
            if capacity > 0:
                valid_capacity = True
            else:
                print("Please enter a valid size.")
        except ValueError:
            print("Please enter a valid size.")
    # initialize pakudex
    pakudex = Pakudex(capacity)
    print(f"The Pakudex can hold {pakudex.capacity} species of Pakuri.")
    # start main_loop
    program_run = True
    while program_run:
        # menu loop
        valid_input = False
        while not valid_input:
            # print menu
            print_pakudex_menu()
            # prompt for input            
            choice = input("What would you like to do? ")
            # check valid input
            try:
                choice = int(choice)
                if 1 <= choice <= 6:
                    valid_input = True
                else:
                    print("Unrecognized menu selection!")
            except ValueError:
                print("Unrecognized menu selection!")
        # choice = menu selection    
        match choice:
            # list pakuri
            case 1:
                # attempt to get list. None if pakudex is empty
                species_list = pakudex.get_species_array()
                if species_list == None:
                    print("No Pakuri in Pakudex yet!")
                else:
                    print("Pakuri In Pakudex: ")
                    for i in range(len(species_list)):
                        num = i+1
                        species = species_list[i]
                        print(f"{num}. {species}")
            # show pakuri
            case 2:
                species = input("Enter the name of the species to display: ")
                # get stats. None if species not found 
                stats = pakudex.get_stats(species)
                if stats == None:
                    print("Error: No such Pakuri!")
                else:
                    print(f"\nSpecies: {species}")
                    print(f"Attack: {stats[0]}")
                    print(f"Defense: {stats[1]}")
                    print(f"Speed: {stats[2]}")
            # add pakuri
            case 3:
                # check if full
                if pakudex.get_size() == pakudex.get_capacity():
                    print("Error: Pakudex is full!")
                else:
                    species = input("Enter the name of the species to add: ")
                    # attempt to add species. True if success, False if duplicate.
                    added = pakudex.add_pakuri(species)
                    if added:
                        print(f"Pakuri species {species} successfully added!")
                    else:
                        print("Error: Pakudex already contains this species!")                    
            # evolve pakuri
            case 4:
                species = input("Enter the name of the species to evolve: ")
                # attempt to evolve, True if success, False if species not found.
                evolved = pakudex.evolve_species(species)
                if evolved:
                    print(f"{species} has evolved!")
                else:
                    print("Error: No such Pakuri!")
            # sort pakuri
            case 5:
                pakudex.sort_pakuri()
                print("Pakuri have been sorted!")
            # exit program
            case 6:
                print("Thanks for using Pakudex! Bye!")
                program_run = False


if __name__ == '__main__':
    main()
