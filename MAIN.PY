import random

def display_board(board):
    print("-------" * 3 + '+')
    for row in board:
        print('|        ' * 3 + '|')
        for cell in row:
            print(f"|   {cell}  ", end="")
        print("|")
        print('|        ' * 3 + '|')
        print("-------" * 3 + '+')

def enter_move(board):
    while True:
        move = input("Enter num value from (1-9): ")
        if move.isdigit():
            move = int(move)
            if not (1 <= move <= 9):
                print("Number must be between 1 and 9.")
                continue
            row = (move - 1) // 3
            col = (move - 1) % 3
            if board[row][col] in ["X", "O"]:
                print("That space is already taken.")
                continue
            board[row][col] = 'O'
            break
        else:
            print("Invalid input. Please enter a number from 1 to 9.")

def make_list_of_free_fields(board):
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X', 'O']:
                free_fields.append((row, col))
    return free_fields

def victory_for(board, sign):
    # Check rows
    for row in board:
        if all(cell == sign for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == sign for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == sign for i in range(3)):
        return True
    if all(board[i][2 - i] == sign for i in range(3)):
        return True
    return False

def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, col = random.choice(free_fields)
        board[row][col] = 'X'

# Initial board
board = [
    ['1', '2', '3'],
    ['4', 'X', '6'],
    ['7', '8', '9']
]

# Game loop
while True:
    # Player's move
    enter_move(board)
    display_board(board)
    if victory_for(board, 'O'):
        print("Congratulations! You win!")
        break
    elif not make_list_of_free_fields(board):
        print("It's a draw!")
        break

    # Computer's move
    draw_move(board)
    display_board(board)
    if victory_for(board, 'X'):
        print("Computer wins! Better luck next time.")
        break
    elif not make_list_of_free_fields(board):
        print("It's a draw!")
        break
