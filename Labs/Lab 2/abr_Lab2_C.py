## give user currency options A, B, and C

print("Available Currencies: A)USD B)CAD C)YEN")

## input a positive dollar amount
amount = float(input("Enter transaction amount: "))

## input given currency
given = input("Transaction currency: ")

## input desired currency
desired = input("Currency to convert to: ")

if given != desired:
    # convert USD to either CAD or YEN
    if given == 'A':
        if desired == 'B':
            amount *= (1.24/1)
            currency_symbol = "CAD"
        elif desired == 'C':
            amount *= (108.59/1)
            currency_symbol = "JPY"
    # convert CAD to either USD or YEN
    elif given == 'B':
        if desired == 'A':
            amount *= (1/1.24)
            currency_symbol = "USD"
        elif desired == 'C':
            amount *= (108.59/1.24)
            currency_symbol = "YEN"
    # convert YEN to either USD or CAD
    elif given == 'C':
        if desired == 'A':
            amount *= (1/108.59)
            currency_symbol = "USD"
        elif desired == 'B':
            amount *= (1.24/108.59)
            currency_symbol = "CAD"
    # print rounded value along with it's respective currency symbol                
    print(f"Converted value: {round(amount,2)} {currency_symbol}")
    
## if converting to the same currency print conversion not needed.
elif given == desired:
    print("Conversion not needed...")
    