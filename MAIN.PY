def display_board(board) :
    print("-------"*3+'+')
    for row in board:
        print('|        '*3+'|')
        for cell in row:
            print(f"|   {cell}  ", end="")
        print("|")

        print('|        '*3+'|')
        print("-------"*3+'+')
board = [
    ['1', '2', '3'],
    ['4', 'X', '6'],
    ['7', '8', '9']
]
display_board(board)