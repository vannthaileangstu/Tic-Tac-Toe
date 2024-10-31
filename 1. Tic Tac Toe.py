board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player = 1

# Win Flags
Win = 1
Draw = -1
Working = 0
Stop = 1

Game = Working
Mark = 'X'


def DrawBoard():
    print(" |%a|%a|%a| " % (board[1], board[2], board[3]) +  ("  |'1'|'2'|'3'|"))
    print(" |%a|%a|%a| " % (board[4], board[5], board[6]) +  ("  |'4'|'5'|'6'|"))
    print(" |%a|%a|%a| " % (board[7], board[8], board[9]) +  ("  |'7'|'8'|'9'|"))

def CheckPosition(x):
    if board[x] == ' ':
        return True
    else:
        return False

def CheckWin():
    global Game

    if board[1] == board[2] and board[2] == board[3] and board[1] != ' ':
        Game = Win
    elif board[4] == board[5] and board[5] == board[6] and board[4] != ' ':
        Game = Win
    elif board[7] == board[8] and board[8] == board[9] and board[7] != ' ':
        Game = Win
    elif board[1] == board[4] and board[4] == board[7] and board[1] != ' ':
        Game = Win
    elif board[2] == board[5] and board[5] == board[8] and board[2] != ' ':
        Game = Win
    elif board[3] == board[6] and board[6] == board[9] and board[3] != ' ':
        Game = Win
    elif board[1] == board[5] and board[5] == board[9] and board[5] != ' ':
        Game = Win
    elif board[3] == board[5] and board[5] == board[7] and board[5] != ' ':
        Game = Win
    elif board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and \
            board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and \
            board[7] != ' ' and board[8] != ' ' and board[9] != ' ':
        Game = Draw
    else:
        Game = Working


while Game == Working:
    DrawBoard()

    if player % 2 != 0:
        print("Player 1's turn: X")
        Mark = 'X'
    else:
        print("Player 2's turn: O")
        Mark = 'O'

    choice = int(input("Place your mark location between [1-9]: "))
    if CheckPosition(choice):
        board[choice] = Mark
        player += 1
        CheckWin()


    if Game == Draw:
        print("There is no winner: Game Draw")
    elif Game == Win:
        player -= 1
        if player % 2 != 0:
            print("Player 1 is the winner")
        else:
            print("Player 2 is the winner")