from console_gfx import ConsoleGfx


def to_hex_string(data):
    # 1. Translates data (RLE or raw) a hexadecimal string (without delimiters). This method can also aid debugging
    decimal_to_hex = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
                      8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    hex_string = ""
    for i in data:
        hex_string += decimal_to_hex[i]
    return hex_string


def count_runs(flat_data):
    # 2. Returns number of runs of data in an image data set; double this result for length of encoded (RLE) list.
    runs = 1
    for i in range(len(flat_data)):
        if i==0:
            continue
        previous = flat_data[i-1]
        current = flat_data[i]
        if previous != current:
            runs += 1
    return runs

def encode_rle(flat_data):
    # 3. Returns encoding (in RLE) of the raw data passed in; used to generate RLE representation of a data.
    rlelist = []
    i = 0
    while i < len(flat_data):
        multiples = 1
        while i + 1 < len(flat_data) and flat_data[i] == flat_data[i + 1]:
            multiples += 1
            i += 1
            if multiples == 15:
                break  # Break if we've reached the limit of 15 multiples
        rlelist.append(multiples)
        rlelist.append(flat_data[i])
        i += 1
            
    return rlelist




def get_decoded_length(rle_data):
    # 4. Returns decompressed size RLE data; used to generate flat data from RLE encoding. (Counterpart to #2)
    length = 0
    for i in range(len(rle_data)):
        if i % 2 == 0:
            length += rle_data[i]
    return length


def decode_rle(rle_data):
    # 5. Returns the decoded data set from RLE encoded data. This decompresses RLE data for use. (Inverse of #3)
    flatlist = []
    for i in range(len(rle_data)):
        if i % 2 == 0:
            continue
        multiples = rle_data[i - 1]
        value = rle_data[i]
        for j in range(multiples):
            flatlist.append(value)
    return flatlist
            


def string_to_data(data_string):
    # 6. Translates a string in hexadecimal format into byte data (can be raw or RLE). (Inverse of #1)
    hex_to_decimal = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                      '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    data = []
    for i in data_string:
        data.append(hex_to_decimal[i])
    return data


def to_rle_string(rle_data):
    # 7. Translates RLE data into a human-readable representation. For each run, in order, it should display the run
    #    length in decimal (1-2 digits); the run value in hexadecimal (1 digit); and a delimiter, ‘:’, between runs.
    decimal_to_hex = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
                      8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    
    data_formatted = []
    for i in range(len(rle_data)):
        if i % 2 == 0:
            count = rle_data[i]
            if count > 15:
                while count > 15:
                    data_formatted.extend([str(15), decimal_to_hex[rle_data[i + 1]], ":"])
                    count -= 15
                data_formatted.extend([str(count), decimal_to_hex[rle_data[i + 1]], ":"])
            else:
                data_formatted.extend([str(count), decimal_to_hex[rle_data[i + 1]], ":"])
    
    # Remove the last delimiter
    data_formatted.pop()
    
    # Convert the list to a string
    rle_string = ''.join(data_formatted)
    
    return rle_string


def string_to_rle(rle_string):
    # 8. Translates a string in human-readable RLE format (with delimiters) into RLE byte data. (Inverse of #7)
    hex_to_decimal = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                      '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    
    sloppy_rle_data = []
    for i in rle_string:
        sloppy_rle_data.append(i)
    
    sloppy_rle_data.append(":")
    
    # search for every delimiter (thats why i added one to the end)
    rle_data = []
    for i in range(len(sloppy_rle_data)):
        if sloppy_rle_data[i] != ":":
            continue

        hex_digit = sloppy_rle_data[i-1]
        decimal_digit = sloppy_rle_data[i-2]
        if i-2 != 0:
            potential_decimal_digit = sloppy_rle_data[i-3]
            if potential_decimal_digit != ":":
                decimal_digit = f'{potential_decimal_digit}{decimal_digit}'

        hex_digit = hex_to_decimal[hex_digit]
        
        rle_data.append(int(decimal_digit))
        rle_data.append(hex_digit)

    
    return rle_data


def main():
    program_run = True
    print("Welcome to the RLE image encoder! \n")
    print("Displaying Spectrum Image: ")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)
    while program_run:
        print("\nRLE Menu")
        print("--------")
        print("0. Exit")
        print("1. Load File")
        print("2. Load Test Image")
        print("3. Read RLE String")
        print("4. Read RLE Hex String")
        print("5. Read Data Hex String")
        print("6. Display Image")
        print("7. Display RLE String")
        print("8. Display Hex RLE Data")
        print("9. Display Hex Flat Data")
        selection = input("\nSelect a Menu Option: ")

        try:
            selection = int(selection)
            if 0 <= selection <= 9:
                match selection:
                    case 0:
                        # Exit
                        program_run = False
                        break
                    case 1:
                        # Load File
                        filename = input("Enter name of file to load: ")
                        image_data = ConsoleGfx.load_file(filename)
                        flat_byte_data = image_data
                    case 2:
                        # Load Test Image
                        image_data = ConsoleGfx.test_image
                        print("Test image data loaded.")
                        flat_byte_data = image_data
                    case 3:
                        # Read RLE String
                        rle_string = input("Enter an RLE string to be decoded: ")
                        flat_byte_data = decode_rle(string_to_rle(rle_string))
                    case 4:
                        # Read RLE Hex String
                        rle_hex_string = input("Enter the hex string holding RLE data: ")
                        flat_byte_data = decode_rle(string_to_data(rle_hex_string))
                    case 5:
                        # Read Data Hex String
                        data_hex_string = input("Enter the hex string holding flat data: ")
                        flat_byte_data = string_to_data(data_hex_string)
                    case 6:
                        # Display Image
                        print("Displaying image...")
                        try: 
                            ConsoleGfx.display_image(image_data)
                        except UnboundLocalError:
                            print("(no data)")
                    case 7:
                        # Display RLE String
                        try:
                            rle_string = to_rle_string(encode_rle(flat_byte_data))
                            print(f"RLE representation: \n{rle_string}")
                        except UnboundLocalError:
                            print("RLE representation: (no data)")
                    case 8:
                        # Display Hex RLE Data
                        try:
                            hex_rle_data = to_hex_string(encode_rle(flat_byte_data))
                            print(f"RLE hex values: \n{hex_rle_data}")

                        except UnboundLocalError:
                            print("RLE hex values: (no data)")
                    case 9:
                        # Display Hex Flat Data
                        try:
                            hex_flat_data = to_hex_string(flat_byte_data)
                            print(f"Flat hex values: \n{hex_flat_data}")
                        except UnboundLocalError:
                            print("Flat hex values: (no data)")
            else:
                # Invalid Input
                print("Error! Invalid input.")
        except ValueError:
            # Invalid Input
            print("Error! Invalid input.")


if __name__ == "__main__":
    main()
