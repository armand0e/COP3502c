# Print main menu
print("Available movies today:")
print("A)12 Strong:   1)2:30  2)4:40 3)7:50 4)10:50")
print("B)Coco:        1)12:40 2)3:45")
print("C)The Post:    1)12:45 2)3:35 3)7:05 4)9:55")

# Gather user inputs
## user inputs movie choice (A,B, or C)
movie = input("Movie choice:  ")
## input desired showtime
showtime = int(input("Showtime:      ")) - 1


# Use math
if movie == "A":
    showtimes = [14.50, 16.66, 19.83, 22.83]
elif movie == "B":
    showtimes = [12.66, 15.75]
elif movie == "C":
    showtimes = [12.75, 15.58, 19.08, 21.92]
else:
    print("Invalid option; please restart app...")

try:
    showtime = showtimes[showtime]
    if showtime <= 14.00:
        adult_price = 11.17
        child_price = 8.00
    elif showtime > 14.00:
        adult_price = 12.45
        child_price = 9.68
    ## no. of tickets (child and adult)
    adults = int(input("Adult tickets: "))
    kids = int(input("Kid tickets:   "))
    if adults + kids <= 30:
        total = (adults * adult_price) + (kids * child_price)
        print(f"Total cost:    ${round(total, 2)}")
    else: 
        print("Invalid option; please restart app...")
except NameError:
    pass
except IndexError:
    print("Invalid option; please restart app...")