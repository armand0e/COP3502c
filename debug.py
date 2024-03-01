data_string = '3f64'
# 6. Translates a string in hexadecimal format into byte data (can be raw or RLE). (Inverse of #1)
hex_to_decimal = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                  '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
data = []
for i in data_string:
    data.append(hex_to_decimal[i])

print(data)