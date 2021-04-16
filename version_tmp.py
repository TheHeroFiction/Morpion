
"""
Coder par ZedRoff et TheHeroFiction en 2021.
Projet NSI.
Version 1.0.0
Tous droits réservés
"""

# Modules

from tkinter import *
import random

# Init

win = Tk()
main_color = "#0B243B"
version = "1.0.0"

win.configure(bg=main_color)
win.title("Morpion {}".format(version))
win.minsize(500, 500)

# Body

frame1 = Frame(win,bg="#0B0B61")
frame1.pack(side=TOP, fill='x')

title = Label(frame1, text="Morpion", bd="5", relief=SUNKEN, font="Verdana 25 bold", fg="white", bg=main_color)
title.pack(pady=25)

hr = Frame(frame1, bg="white", width="450px", height="5px")
hr.pack(pady=25)

frame2 = Frame(win,bg=main_color)
frame2.pack(side=BOTTOM, fill='x')
frame3 = Frame(win, bg="red")

w_btn = 5
h_btn = 5
c_btn = main_color


turn = random.randint(0,1)
print(turn)
tab = [[0,0,0],[0,0,0],[0,0,0]]

g = []
b1, b2, b3, b4, b5, b6, b7, b8, b9, b10 = Button(frame3, width=w_btn, height=h_btn, bg=c_btn, activebackground=main_color, command=lambda: click(0,0)),Button(frame3, width=w_btn, height=h_btn, bg=c_btn, command=lambda: click(0,1), activebackground=main_color),Button(frame3, width=w_btn, height=h_btn, bg=c_btn, command=lambda: click(0,2), activebackground=main_color),Button(frame3, width=w_btn, height=h_btn, bg=c_btn, command=lambda: click(1,0), activebackground=main_color),Button(frame3, width=w_btn, height=h_btn, bg=c_btn, command=lambda: click(1,1), activebackground=main_color),Button(frame3, width=w_btn, height=h_btn, bg=c_btn, command=lambda: click(1,2), activebackground=main_color),Button(frame3, width=w_btn, height=h_btn, bg=c_btn, command=lambda: click(2,0), activebackground=main_color),Button(frame3, width=w_btn, height=h_btn, bg=c_btn, command=lambda: click(2,1), activebackground=main_color),Button(frame3, width=w_btn, height=h_btn, bg=c_btn, command=lambda: click(2,2), activebackground=main_color),Button(frame2, width=1, height=1, bg=c_btn, highlightthickness=0,bd=0)
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=1, column=0, pady=5)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=2,column=0)
b8.grid(row=2, column=1, padx=5)
b9.grid(row=2, column=2)
b10.grid(row=2, column=2)

g.append([[b1, b2, b3], [b4, b5, b6], [b7, b8, b9]])
print(g[0][0][0])


def checker(c):
    global tab, g
    if c == 0:
        print()
        print("O won.")
        tab = [[0,0,0], [0,0,0], [0,0,0]]
        for i in range(len(g)):
            for j in range(len(len(g[i]))):
                print(g[i][j])
    elif c == 1:
        print()
        print("X won.")
        tab = [[0,0,0], [0,0,0], [0,0,0]]
    else:
        pass

def verif(arr, changer):
    if arr[0][0] == arr[1][1] == arr[2][2]  != 0:
        checker(changer)
    
    elif arr[2][0] == arr[1][1] == arr[0][2] != 0:
        checker(changer)
  
    elif arr[0][0] == arr[0][1] == arr[0][2] != 0:
        checker(changer)
  
    elif arr[1][0] == arr[1][1] == arr[1][2] != 0:
        checker(changer)
  
    elif arr[2][0] == arr[2][1] == arr[2][2] != 0:
        checker(changer)
      
    elif arr[0][0] == arr[1][0] == arr[2][0] != 0:
        checker(changer)
       
    elif arr[0][1] == arr[1][1] == arr[2][1] != 0:
        checker(changer)
   
    elif arr[0][2] == arr[1][2] == arr[2][2] != 0:
        checker(changer)
        
    else:
        pass

def click(x, y):
    global turn
    if turn == 0:
        tab[x][y] = "X"
        turn=1
  
        g[0][x][y]["text"] = "X"
        g[0][x][y]["fg"] = "white"
        verif(tab, turn)
        print(tab)
    else:
        tab[x][y] = "O"
        turn=0
  
        g[0][x][y]["text"] = "O"
        g[0][x][y]["fg"] = "white"
        verif(tab, turn)
b10.bind("<Button-1>", func=lambda rien: messagebox.showinfo("Easter Egg", "Vous avez trouvé le boutton caché o_O"))
b10.bind("<Enter>", func=lambda rien: b10.config(activeButton=main_color))
frame3.pack(expand=1)

# Shower

win.mainloop()
