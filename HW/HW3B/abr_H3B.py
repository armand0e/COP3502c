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
    pass


def encode_rle(flat_data):
    # 3. Returns encoding (in RLE) of the raw data passed in; used to generate RLE representation of a data.
    pass


def get_decoded_length(rle_data):
    # 4. Returns decompressed size RLE data; used to generate flat data from RLE encoding. (Counterpart to #2)
    pass


def decode_rle(rle_data):
    # 5. Returns the decoded data set from RLE encoded data. This decompresses RLE data for use. (Inverse of #3)
    pass


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
    #    (See examples in standalone section.)
    pass


def string_to_rle(rle_string):
    # 8. Translates a string in human-readable RLE format (with delimiters) into RLE byte data. (Inverse of #7)
    pass


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
                    case 2:
                        # Load Test Image
                        image_data = ConsoleGfx.test_image
                        print("Test image data is loaded")
                    case 3:
                        # Read RLE String
                        pass
                    case 4:
                        # Read RLE Hex String
                        pass
                    case 5:
                        # Read Data Hex String
                        pass
                    case 6:
                        # Display Image
                        ConsoleGfx.display_image(image_data)
                    case 7:
                        # Display RLE String
                        pass
                    case 8:
                        # Display Hex RLE Data
                        pass
                    case 9:
                        # Display Hex Flat Data
                        pass
            else:
                # Invalid Input
                print("Invalid input! Please enter an integer 0-9.")
        except ValueError:
            # Invalid Input
            print("Invalid input! Please enter an integer 0-9.")


if __name__ == "__main__":
    main()
