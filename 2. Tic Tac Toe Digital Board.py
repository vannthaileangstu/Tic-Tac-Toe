import tkinter
window = tkinter.Tk()
window.title("Tic Tac Toe Game")
frame = tkinter.Frame(window)
frame.pack()
label = tkinter.Label(frame,font=("consulas", 50,"bold"))
label.pack()


window.update()
window.mainloop()