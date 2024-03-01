def hex_char_decode(digit):
    # Decodes a single hexadecimal digit and returns its value.
    hex_to_decimal = {'0': 0, '1': 1, '2': 2, '3': 3,
                      '4': 4, '5': 5, '6': 6, '7': 7,
                      '8': 8, '9': 9, 'A': 10, 'B': 11,
                      'C': 12, 'D': 13, 'E': 14, 'F': 15}
    value = hex_to_decimal[digit]
    return value


def hex_string_decode(hex):
    # Decodes an entire hexadecimal string and returns its value.
    value = 0
    hex_length = len(hex) - 1
    for i in hex:
        value = value + (hex_char_decode(i) * (16 ** hex_length))
        hex_length = hex_length - 1
    return value


def hex_encode(value):
    # Encodes an entire hexadecimal string from a given value
    decimal_to_hex = {0: '0', 1: '1', 2: '2', 3: '3',
                      4: '4', 5: '5', 6: '6', 7: '7',
                      8: '8', 9: '9', 10: 'A', 11: 'B',
                      12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    hexstr = ''
    while (value > 0):
        remainder = value % 16
        hexstr = decimal_to_hex[remainder] + hexstr
        value = value // 16

    return hexstr


def binary_string_decode(binary):
    # Decodes a binary string and returns its value.
    binary = int(binary)
    value = 0
    i = 0
    while (binary != 0):
        remainder = binary % 10
        value = value + remainder * (2 ** i)
        binary = binary // 10
        i += 1
    return value


def binary_to_hex(binary):
    # Decodes a binary string, re-encodes it as hexadecimal, and returns the hexadecimal string.
    value = binary_string_decode(binary)
    hex = hex_encode(value)
    return hex


def print_main_menu():
    print("Decoding Menu")
    print("-------------")
    print("1. Decode hexadecimal")
    print("2. Decode binary")
    print("3. Convert binary to hexadecimal")
    print("4. Quit\n")


def main():
    programrun = True
    while programrun:
        valid_input = False
        print_main_menu()
        while not valid_input:
            choice = input("Please enter an option: ")
            try:
                choice = int(choice)
                if 1 <= choice <= 4:
                    valid_input = True
                else:
                    print("Invalid Input! Please choose an integer 1-4\n")
            except:
                print("Invalid Input! Please choose an integer 1-4\n")

        match choice:
            case 1:  # Decode hexadecimal
                hexstring = input("Please enter the numeric string to convert: ").strip().upper()
                hexstringlist = []
                for i in hexstring:
                    hexstringlist.append(i)
                if hexstring[0] == "0" and hexstring[1] == "X":
                    hexstringlist.pop(0)
                    hexstringlist.pop(0)
                elif hexstring[0] == "0" and hexstring[1] == "B":
                    hexstringlist.pop(0)
                    hexstringlist.pop(0)
                hexstring = ""
                for i in hexstringlist:
                    hexstring += i
                print(f"Result: {hex_string_decode(hexstring)}\n")

            case 2:  # Decode binary
                binarystring = input("Please enter the numeric string to convert: ").strip().upper()
                binarystringlist = []
                for i in binarystring:
                    binarystringlist.append(i)
                if binarystring[0] == "0" and binarystring[1] == "X":
                    binarystringlist.pop(0)
                    binarystringlist.pop(0)
                elif binarystring[0] == "0" and binarystring[1] == "B":
                    binarystringlist.pop(0)
                    binarystringlist.pop(0)
                binarystring = ""
                for i in binarystringlist:
                    binarystring += i
                print(f"Result: {binary_string_decode(binarystring)}\n")

            case 3:  # Convert binary to hexadecimal
                binarystring = input("Please enter the numeric string to convert: ").strip().upper()
                binarystringlist = []
                for i in binarystring:
                    binarystringlist.append(i)
                if binarystring[0] == "0" and binarystring[1] == "X":
                    binarystringlist.pop(0)
                    binarystringlist.pop(0)
                elif binarystring[0] == "0" and binarystring[1] == "B":
                    binarystringlist.pop(0)
                    binarystringlist.pop(0)
                binarystring = ""
                for i in binarystringlist:
                    binarystring += i
                print(f"Result: {binary_to_hex(binarystring)}\n")

            case 4:  # Quit
                programrun = False
                break


if __name__ == '__main__':
    main()
