import tkinter
from tkinter import *
from os import*

def sleepclick():
   print(system("shutdown /h"))
def shutdownclick():
   print(system("shutdown /s /t 0"))
def restartclick():
   print(system("shutdown /r /t 0"))

root = tkinter.Tk()
root.geometry("400x305")

photo = PhotoImage(file="sleep.png")
photo2 = PhotoImage(file="shutdown.png")
photo3 = PhotoImage(file="restart.png")
btn = Button(
    root,
    image=photo,
    command=sleepclick,
    border=0,
)
btn.pack(pady=30)
btn2 = Button(
    root,
    image=photo2,
    command=shutdownclick,
    border=0,
)
btn2.pack()
btn3 = Button(
    root,
    image=photo3,
    command=restartclick,
    border=0,
)
btn3.pack( pady=30)

text = Text(root)
text.insert(INSERT, ">>>S.M.Nurnobi")
text.pack()

root.mainloop()
