board = [['.','.','.'],
         ['.','.','.'],
         ['.','.','.']]

def print_board():
    print(board[0])
    print(board[1])
    print(board[2])

def play():
    pass


#main program ------
def player():
    player = (int(input("Would you like 1 or 2? ")))
    if player == str(1):
        player_one = print("You are Player 1: x")
        print(player_one)
        print(player)
    if player == str(2):
        print("You are Player 2: o")
    
#print_instruction()

print_board()
#If no winner than repeat
print_board()
play()
player()
#check_winner()


