# Print main menu
print("Available movies today:")
print("A)12 Strong:   1)2:30  2)4:40 3)7:50 4)10:50")
print("B)Coco:        1)12:40 2)3:45")
print("C)The Post:    1)12:45 2)3:35 3)7:05 4)9:55")

# Gather user inputs
## user inputs movie choice (A,B, or C)
movie = input("Movie choice:  ")
showtime = int(input("Showtime: "))
showtimes = []
if movie == "A":
    showtimes = [14.50, 16.66, 19.83, 22.83]
elif movie == "B":
    showtimes = [12.66, 15.75]
elif movie == "C":
    showtimes = [12.75, 15.58, 19.08, 21.92]
else:
    print("Invalid option; please restart app...")

print(showtimes)

