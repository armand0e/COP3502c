import sys
from heifer_generator import HeiferGenerator

def list_cows(cows):
    # Displays the available cows from a Python list of Cow objects.
    pass

def find_cow(name, cows):
    # Given a name and a Python list of Cow objects, return the Cow object with the specified name. If no such Cow object can be found, return None.
    pass

def main():
    cows = HeiferGenerator.get_cows()
    if sys.argv[1] == '-l':
        list_cows(cows)
    elif sys.argv[1] == '-n':
        try:
            cow = sys.argv[2]
            message = ""
            for i in range(len(sys.argv)):
                if i < 3:
                    continue
                message += sys.argv[i]
            cow = find_cow(cow, cows)
            print(f"cow: {cow}\nmessage: {message}")
        except IndexError:
            print("Error: Missing arguements!")
            print("Try: cowsay.py -n <cow> <message>")

if __name__ == '__main__':
    main()
