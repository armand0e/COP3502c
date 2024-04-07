import sys
from heifer_generator import HeiferGenerator
from cow import Cow

def list_cows(cows):
    # Displays the available cows from a Python list of Cow objects.
    cow_list = ""
    for cow in cows:
        
        cow_list += Cow.get_name(cow) + " "
    print(f"Cows available: {cow_list}")

def find_cow(name, cows):
    # Given a name and a Python list of Cow objects, return the Cow object with the specified name. If no such Cow object can be found, return None.
    for i in cows:
        if Cow.get_name(i) == name:
            return i
    return None
        
    pass

def main():
    cows = HeiferGenerator.get_cows()
    try:
        if sys.argv[1] == '-l':
            list_cows(cows)
        elif sys.argv[1] == '-n':
            try:
                name = sys.argv[2]
                message = ""
                for i in range(len(sys.argv)):
                    if i < 3:
                        continue
                    message += sys.argv[i] + " "
                cow = find_cow(name, cows)
                if cow == None:
                    print(f"Could not find {name} cow!")
                else:
                    print("")
                    print(message)
                    print(Cow.get_image(cow))
                    
            except IndexError:
                print("Error: Missing arguments!")
                print("Try: ") 
                print(" python3 cowsay.py -n <cow> <message>")
        elif sys.argv[1] != "-l" and sys.argv[1] != "-n":
            cow = find_cow("heifer", cows)
            message = ""
            for i in range(len(sys.argv)):
                if i < 1:
                    continue
                message += sys.argv[i] + " "
            print("")
            print(message)
            print(Cow.get_image(cow))
    except IndexError:
        print("Error: Missing arguments!")
        print("Try: ")
        print(" python3 cowsay.py -l")
        print(" python3 cowsay.py <message>") 
        print(" python3 cowsay.py -n <cow> <message>")

if __name__ == '__main__':
    main()
