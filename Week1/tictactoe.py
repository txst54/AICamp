import os

print("Welcome to tic tac toe")
print("Each player should enter a number from one through nine. Each number corresponds to a cell on the board going from left to right.")
print("Press Enter to continue")
input()
size = 3
board = [['_' for i in range(size)] for j in range(size)]
winner = None
currentPlayer = 'X'

def drawBoard():
    col = 0
    for row in board:
        for i in row:
            print(i, end = " ")
        print("\n")

def checkForWinners():
    #check rows and columns
    for n in range(len(board)):
        row = board[n]
        col = [board[i][n] for i in range(len(board))]
        if '_' not in col and col.count(col[0]) == len(col):
            return col[0]
            break
        elif '_' not in row and row.count(row[0]) == len(row):
            return row[0]
            break

    #check for diagonals
    diag1 = [board[i][i] for i in range(len(board))]
    diag2 = [board[len(board) - (i + 1)][i] for i in range(len(board))]
    if (diag1[0] != '_' and diag1.count(diag1[0]) == len(diag1)) or (diag2[0] != '_' and diag2.count(diag2[0]) == len(diag2)):
        return diag1[1]

    #Check for tie
    containsBlank = ['_' in row for row in board]
    if True not in containsBlank:
        return "draw"
    
while winner == None:
    drawBoard()
    print(f"It is Player {currentPlayer}'s turn")

    while True:
        move = int(input("Enter your move: ")) - 1
        if move >= 0 and move <= (size ** 2) - 1 and board[int(move/3)][move % 3] == '_':
            board[int(move / size)][move % size] = currentPlayer
            break
        else:
            print("Invalid move, please reenter move")

    if currentPlayer == 'X':
        currentPlayer = 'O'
    elif currentPlayer == 'O':
        currentPlayer = 'X'
    winner = checkForWinners()

drawBoard()
if winner != "draw":
    print(f"Congratulations Player {winner}")
else:
    print("Draw")
