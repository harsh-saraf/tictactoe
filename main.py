# define variables

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
currentPlayer = "X"
winner = None
gameRunning = True

#  print the game board

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])       

# printBoard(board)

# take user input and edit board

def PlayerInput(board):
    inp = int(input("Enter a number from 1 to 9: "))
    if inp >=1 and inp <=9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Oops, try again!")
        SwitchPlayer()

# evaluate victory scenarios (if else loop)

def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = currentPlayer
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = currentPlayer
        return True    
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = currentPlayer
        return True


def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = currentPlayer
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = currentPlayer
        return True    
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = currentPlayer
        return True


def checkDiagnol(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = currentPlayer
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = currentPlayer
        return True    


def checkTie(board):
    global gameRunning
    if not(checkHorizontal(board)) and not(checkVertical(board)) and not(checkDiagnol(board)):
        if "-" not in board:
            printBoard(board)
            print("It is a tie")
            gameRunning = False

def checkWin():
    if checkHorizontal(board) or checkVertical(board) or checkDiagnol(board):
        print(f"The winner is {winner}")
        gameRunning = False

#switch the player

def SwitchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

#print final message and end game

while gameRunning:
    printBoard(board)
    if winner!=None:
        break
    PlayerInput(board)
    checkWin()
    checkTie(board)
    SwitchPlayer()