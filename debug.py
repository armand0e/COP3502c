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
        for row in range(len(board[i])):
            if board[row-1][col] == '-':
                board[row-1][col] = chip_type
                break


def main():
    cols = 5
    rows = 4
    board = initialize_board(rows, cols)
    print_board(board)
    chip = 'x'

    col = int(input('choose column'))
    insert_chip(board, col, chip)
    print_board(board)


if __name__ == '__main__':
    main()