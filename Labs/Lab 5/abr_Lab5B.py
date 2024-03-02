def print_board(board):
    for i in range(len(board)):
        row = ""
        for j in range(len(board[i])):
            row += board[i][j] + " "
        print(row)


def initialize_board(num_rows, num_cols):
    board = [['-'] * num_cols] * num_rows
    return board


def insert_chip(board, col, chip_type):
    for i in range(len(board)):
        # parse from the bottom row up
        neg_i = len(board) - i - 1
        if board[neg_i][col] == '-':
            board[neg_i][col] = chip_type
            break

    return board


def check_if_winner(board, col, row, chip_type):
    pass


def main():
    invalid_input = True
    while invalid_input:
        try:
            rows = int(input("What would you like the height of the board to be? "))
            cols = int(input("What would you like the length of the board to be? "))
            if rows >= 4 and cols >= 4:
                invalid_input = False
            else:
                invalid_input = True
                print("\nInvalid input! Please input an integer greater than or equal to 4")
        except ValueError:
            print("\nInvalid input! Please input an integer greater than or equal to 4")
            invalid_input = True

    turns = 0
    board = initialize_board(rows, cols)
    print_board(board)
    print("\nPlayer 1: x")
    print("Player 2: o")

    keep_playing = True
    while keep_playing:
        if turns % 2 == 0:
            chip = 'x'
            invalid_input = True
            while invalid_input:
                try:
                    desired_column = int(input("\nPlayer 1: Which column would you like to choose? "))
                    if 0 <= desired_column <= cols - 1:
                        invalid_input = False
                    else:
                        print(f"\nInvalid input! Please choose an integer from 0-{cols - 1}")
                        invalid_input = True
                except ValueError:
                    print(f"\nInvalid input! Please choose an integer from 0-{cols - 1}")
                    invalid_input = True

        elif turns % 2 == 1:
            chip = 'o'
            invalid_input = True
            while invalid_input:
                try:
                    desired_column = int(input("\nPlayer 2: Which column would you like to choose? "))
                    if 0 <= desired_column <= cols - 1:
                        invalid_input = False
                    else:
                        print(f"\nInvalid input! Please choose an integer from 0-{cols - 1}")
                        invalid_input = True
                except ValueError:
                    print(f"\nInvalid input! Please choose an integer from 0-{cols - 1}")
                    invalid_input = True
                    # chip is assigned to respective player, chip = 'x' or chip = 'o'
        # chosen column # is stored in desired_column
        board = insert_chip(board, desired_column, chip)
        print_board(board)
        turns += 1


if __name__ == '__main__':
    main()
