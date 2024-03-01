from ast import match_case
from hmac import new
from p1_random import P1Random

def print_menu():
    print("\n1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit\n")
# put this into a method because why not


def invalid_input():
    print("\nInvalid input!\nPlease enter an integer value between 1 and 4.")
# put this into a method too, lol
    

# forgot how to do the def Main() thingy so im just gonna start here
wins = 0
losses = 0
ties = 0
program_run = True
card_name = { 1:"ACE", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"10", 11:"JACK", 12:"QUEEN", 13:"KING" } # made this to make it easy to call the name of any card from it's value
game_number = 1
rng = P1Random()
while program_run == True:
    
    hand_value = 0
    same_game = True
    print(f"START GAME #{game_number}")
    cardID = rng.next_int(13) + 1
    if cardID > 10:
        card_value = 10
    else:
        card_value = cardID
    hand_value += card_value
    print_hand = True
    print(f"\nYour card is a {card_name[cardID]}!")
    print(f"Your hand is: {hand_value}")
    while same_game:
        print_menu()
        user_input = int(input("Choose an option: "))
        if user_input == 1:
            cardID = rng.next_int(13) + 1
            if cardID > 10:
                card_value = 10
            else:
                card_value = cardID
            hand_value += card_value
            if print_hand == True:
                print(f"\nYour card is a {card_name[cardID]}!")
                print(f"Your hand is: {hand_value}")
            if hand_value == 21:
                print("\nBLACKJACK! You win!\n")
                wins += 1
                same_game = False
            if hand_value > 21:
                print("\nYou exceeded 21! You lose.\n")
                losses += 1
                same_game = False
            print_hand = True
        elif user_input == 2:
            dealers_hand = rng.next_int(11) + 16
            print(f"\nDealer's hand: {dealers_hand}")
            print(f"Your hand is: {hand_value}\n")
            if dealers_hand > 21:
                print("You win!\n")
                wins += 1
                same_game = False
            elif dealers_hand == hand_value:
                print("It's a tie! No one wins!\n")
                ties += 1
                same_game = False
            elif dealers_hand > hand_value:
                print("Dealer wins!\n")
                losses += 1
                same_game = False
            print_hand = True
        elif user_input == 3:
            games_played = game_number -1
            print(f"\nNumber of Player wins: {wins}")
            print(f"Number of Dealer wins: {losses}")
            print(f"Number of tie games: {ties}")
            print(f"Total # of games played is: {games_played}")
            win_percentage = 100*(wins/games_played)
            print(f"Percentage of Player wins: {win_percentage:.1f}%")
            print_hand = False
        elif user_input == 4:
            same_game = False
            program_run = False
        else:
            invalid_input()
            print_hand = False
        
    game_number += 1
    