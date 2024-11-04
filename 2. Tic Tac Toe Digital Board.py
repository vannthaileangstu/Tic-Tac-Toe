from tkinter import *
import random

Grey = "#0F0F0F"
Black = "#000000"
White = "#ffffff"
Red = "#FF0000"
Green = "#008000"
Blue = "#0000FF"
Yellow = "#FFFF00"

window = Tk()
window.title("Vannthai's Tic-Tac-Toe")
players = ["x","o"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]


label = Label(text=player + " turn", font=('consolas',30))
label.pack(side="top")


def new_game():
    global player
    player = random.choice(players)
    label.config(text=player+" turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="red")

reset_button = Button(text="Restart", font=('consolas',25), command=new_game)
reset_button.pack(side="bottom")

frame = Frame(window, width=600, height= 600)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('consolas',40), width=5, height=2,
                                      bg="blue" ,command= lambda row=row, column=column: player_turn(row,column))
        buttons[row][column].grid(row=row,column=column)

def player_turn(row, column):
    global player
    if buttons[row][column]['text'] == "" and check_winer() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player
            if check_winer() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"))
            elif check_winer() is True:
                label.config(text=(players[0]+" is the winner"))
            elif check_winer() == "Draw":
                label.config(text="Draw!")
        else:
            buttons[row][column]['text'] = player
            if check_winer() is False:
                player = players[0]
                label.config(text=(players[0]+" turn"))
            elif check_winer() is True:
                label.config(text=(players[1]+" is the winner"))
            elif check_winer() == "Draw":
                label.config(text="Draw!")



def check_winer():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            return True
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return 
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Draw"
    else:
        return False



def empty_spaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True


window.mainloop()