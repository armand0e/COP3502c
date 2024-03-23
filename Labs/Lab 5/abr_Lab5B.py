def print_board(board):
    for i in range(len(board)):
        row = ""
        for j in range(len(board[i])):
            row += board[i][j] + " "
        print(row)


def initialize_board(num_rows, num_cols):
    board = [['-'] * num_cols for _ in range(num_rows)]
    return board


def insert_chip(board, col, chip_type):       
    for i in range(len(board)):
        neg_i = len(board) - i - 1
        if board[neg_i][col] == '-':
            board[neg_i][col] = chip_type
            return neg_i


def check_if_winner(board, col, row, chip_type):
    winner = False
    # check the row that the most recent chip was placed in
    in_a_row = 0
    for i in board[row]:
        if i == chip_type:
            in_a_row += 1
        elif i != chip_type:
            in_a_row = 0
        if in_a_row == 4:
            winner = True
    # check the column that the most recent chip was placed in
    in_a_row = 0
    for i in range(len(board)):
        if board[i][col] == chip_type:
            in_a_row += 1
        elif board[i][col] != chip_type:
            in_a_row = 0
        if in_a_row == 4:
            winner = True
    return winner


def check_if_tie(board):
    tie = True
    for i in board:
        for j in i:
            if j == '-':
                tie = False
    return tie
                


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

    winner = False
    while not winner:
        row = None
        while row == None:
            
            if turns % 2 == 0:
                chip = 'x'
                player = 'Player 1'
                
            elif turns % 2 == 1:
                chip = 'o'
                player = 'Player 2'
                
                
            invalid_input = True
            while invalid_input:
                try:
                    desired_column = int(input(f"\n{player}: Which column would you like to choose? "))
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

            row = insert_chip(board, desired_column, chip)
            if row == None:
                print("\nColumn full! Please select a different column.\n")
            
            print_board(board)
        
        winner = check_if_winner(board, desired_column, row, chip)
        
        if winner:
            print(f"\n{player} won the game!")
            break
        if not winner:
            tie = check_if_tie(board)
            if tie:
                print("\nDraw. Nobody Wins.")
                break

        turns += 1


if __name__ == '__main__':
    main()
