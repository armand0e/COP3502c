
## get water usage in gallons
gallons = int(input("Enter your water usage in gallons: "))


## find charge based on gallons used
if (gallons < 6000): 
    charge = (2.35/1000) 
    debt = gallons * charge
    # this ones simple. gallons * charge

if (6000 <= gallons <= 20000):
    gallons = gallons - 5999
    under6k = 14.1
    # establish the cheaper rate they recieved on the first 5999 gallons
    charge = (3.75/1000)
    debt = under6k + (gallons * charge)
    # add the previous rate's charge with the current
    
if (gallons > 20000):
    gallons = gallons - 5999
    debtunder6k = 14.1
    # under 6k gallons rate
    gallons = gallons - 14001
    debt20k = 52.50375
    # 20k gallons rate
    charge = (6.00/1000)
    debt = debtunder6k + debt20k + (gallons * charge)
    # do it again

## round and print $ owed
debt = round(debt, 2)
print(f"Money owed: ${debt}")