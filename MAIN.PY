def display_board(board) :
    print("-------"*3+'+')
    for row in board:
        print('|        '*3+'|')
        for cell in row:
            print(f"|   {cell}  ", end="")
        print("|")

        print('|        '*3+'|')
        print("-------"*3+'+')
def enter_move(board):
    while True:
        move=input("Enter num value from (1-9): ")
        if move.isdigit():
            move=int(move)
            if 1<=move <=9:
                 print("Number must be between 1 and 9.")
            continue
        row = (move-1)//3
        col = (move-1)%3
        if board[row][col] in ["x","o"]:
            print("That space is already taken.")
            continue
        board[row][col] = 'O'
        break
def make_list_of_free_fields(board):
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in['x',"o"]:
                free_fields.append((row,col))
    return free_fields
   
board = [
    ['1', '2', '3'],
    ['4', 'X', '6'],
    ['7', '8', '9']
]
display_board(board)