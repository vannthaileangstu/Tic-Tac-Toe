import tkinter

current_player = "X"
Grey = "#0F0F0F"
Black = "#000000"
White = "#ffffff"
Red = "#FF0000"
Green = "#008000"
Blue = "#0000FF"
Yellow = "#FFFF00"

board = [[0,0,0],
         [0,0,0], 
         [0,0,0]]

def restart_game():
    print("RESTART")

def tile_click(r, c):
    print(r, c)

window = tkinter.Tk()
window.title("Tic Tac Toe Game")
window.resizable(False, False)

frame = tkinter.Frame(window, width=600, height= 600)
frame.grid_propagate(True)
frame.pack()

message = tkinter.Label(frame, text = current_player+ "'s turn", font=("arial", 30))
message.grid(row=0, column=1)

for  row in range(3):
    for col in range(3):
        board[row][col] = tkinter.Button(frame, text="", font=("arial",50,"bold"), bg=Yellow, fg= Black,
                                         width=4, height=1, name=str(row)+","+str(col), command=lambda r=row,c=col: tile_click(r,c))
        board[row][col].grid(row=row+1, column=col)

restart = tkinter.Button(frame, text = "Restart", font=("arial", 30, "bold"), command=lambda:restart_game())
restart.grid(row=4,column=1)

window.update()
window.mainloop()