# Debug!!!!


def string_to_rle(rle_string):
    # 8. Translates a string in human-readable RLE format (with delimiters) into RLE byte data. (Inverse of #7)
    hex_to_decimal = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                      '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    
    sloppy_rle_data = []
    for i in rle_string:
        sloppy_rle_data.append(i)
    
    sloppy_rle_data.append(":")
    
    # search for every delimiter (thats why i added one to the end)
    last_delimiter_index = 0
    rle_data = []
    for i in range(len(sloppy_rle_data)):
        if sloppy_rle_data[i] != ":":
            continue

        last_delimiter_index = i
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

def string_to_data(data_string):
    # 6. Translates a string in hexadecimal format into byte data (can be raw or RLE). (Inverse of #1)
    hex_to_decimal = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                      '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    data = []
    for i in data_string:
        data.append(hex_to_decimal[i])
    return data            
            
            
            
            
            
            
data = [15, 15, 6, 4]
# should return ^
string = "fff444444"
print(string_to_data(string))