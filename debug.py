data = [3, 15, 6, 4]
# Translates data (RLE or raw) a hexadecimal string (without delimiters). This method can also aid debugging
decimal_to_hex = {  
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
    8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f' 
    }
hexstring = ""
for i in data:
    hexstring += decimal_to_hex[i]

print(hexstring)