"""
Coder par ZedRoff et TheHeroFiction.
Projet NSI.
Version 1.0.0
Tous droits réservés
"""

# Modules

from tkinter import *
import random

# Init

window = Tk()
main_color = "#0B243B"  
version = "1.0.0"

window.configure(bg=main_color)
window.title("Morpion {}".format(version))
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry("{}x{}".format(w, h))


# Body

frame_top = Frame(window, bg="#D65A5A")
frame_top.pack(side=TOP, fill="x")

frame_top_title = Label(
    frame_top,
    text="Morpion",
    bd="5",
    relief=GROOVE,
    font="Verdana 25 bold",
    fg="white",
    bg=main_color,
)
frame_top_title.pack(pady=25)

separator = Frame(frame_top, bg="white", width="450px", height="5px")
separator.pack(pady=25)


frame_middle = Frame(window, bg="#6E83DD", width=650, height=50)
frame_middle_label_left = Label(frame_middle, text="X : 0", fg="white", font="Helvetica 15 bold",bg=main_color)
frame_middle_label_left.place(anchor="e", relx=.1, rely=.5)
frame_middle_label_right = Label(frame_middle, text="O : 0", fg="white", font="Helvetica 15 bold", bg=main_color)
frame_middle_label_right.place(anchor="w", relx=.9, rely=.5)
frame_middle.pack(pady=50)
frame_bottom = Frame(window, bg=main_color)
frame_bottom.pack(side=BOTTOM, fill="x")

table = Frame(window, bg="#F37552", relief=SUNKEN, borderwidth=10)

width_button = 5
height_button = 5
color_button = "#2E2E2E"


turn = random.randint(0, 1)

virtual_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

button_storage = []

(
    button_1,
    button_2,
    button_3,
    button_4,
    button_5,
    button_6,
    button_7,
    button_8,
    button_9,
    button_easter,
) = (
    Button(
        table,
        width=width_button,
        height=height_button,
        bg=color_button,
        activebackground=main_color,
        command=lambda: click(0, 0),
    ),
    Button(
        table,
        width=width_button,
        height=height_button,
        bg=color_button,
        command=lambda: click(0, 1),
        activebackground=main_color,
    ),
    Button(
        table,
        width=width_button,
        height=height_button,
        bg=color_button,
        command=lambda: click(0, 2),
        activebackground=main_color,
    ),
    Button(
        table,
        width=width_button,
        height=height_button,
        bg=color_button,
        command=lambda: click(1, 0),
        activebackground=main_color,
    ),
    Button(
        table,
        width=width_button,
        height=height_button,
        bg=color_button,
        command=lambda: click(1, 1),
        activebackground=main_color,
    ),
    Button(
        table,
        width=width_button,
        height=height_button,
        bg=color_button,
        command=lambda: click(1, 2),
        activebackground=main_color,
    ),
    Button(
        table,
        width=width_button,
        height=height_button,
        bg=color_button,
        command=lambda: click(2, 0),
        activebackground=main_color,
    ),
    Button(
        table,
        width=width_button,
        height=height_button,
        bg=color_button,
        command=lambda: click(2, 1),
        activebackground=main_color,
    ),
    Button(
        table,
        width=width_button,
        height=height_button,
        bg=color_button,
        command=lambda: click(2, 2),
        activebackground=main_color,
    ),
    Button(
        frame_bottom, width=1, height=1, bg=color_button, highlightthickness=0, bd=0
    ),
)

button_1.grid(row=0, column=0)
button_2.grid(row=0, column=1)
button_3.grid(row=0, column=2)
button_4.grid(row=1, column=0, pady=5)
button_5.grid(row=1, column=1)
button_6.grid(row=1, column=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1, padx=5)
button_9.grid(row=2, column=2)


mode = 0
def new_window():
    global mode, menu
    if mode==0:
        menu = Frame(window, width=500, height=500, bg="white", borderwidth=10)
        menu.place(relx=.25, rely=.25)
        mode=1
    else:
        menu.destroy()
        mode=0
    

button_menu = Button(window, text="Menu", command=new_window)
button_menu.place(anchor="e", relx=.9, rely=.9)

button_storage.append(
    [
        [button_1, button_2, button_3],
        [button_4, button_5, button_6],
        [button_7, button_8, button_9],
    ]
)


score_o = 0
score_x = 0

i=0
def checker(c):
    global virtual_board, button_storage, score_o, score_x, i
    if c == 0:
        print()
        print("O won.")
        virtual_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        score_o += 1
        frame_middle_label_right["text"] = "O : {}".format(score_o)
        for i in range(len(button_storage)):
            for j in range(len(button_storage[i])):
                for k in range(len(button_storage[i][j])):

                    button_storage[i][j][k]["text"] = ""
        i=0
    elif c == 1:
        print()
        print("X won.")
        virtual_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        score_x += 1
        frame_middle_label_left["text"] = "X : {}".format(score_x)
        for i in range(len(button_storage)):
            for j in range(len(button_storage[i])):
                for k in range(len(button_storage[i][j])):

                    button_storage[i][j][k]["text"] = ""
        i=0
    elif c == "None":
        print()
        print("Draw")
        virtual_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(len(button_storage)):
            for j in range(len(button_storage[i])):
                for k in range(len(button_storage[i][j])):

                    button_storage[i][j][k]["text"] = ""
        i=0
    else:
        pass
       


def verification_win(board, winner, i):
    if i == 9:
        checker("None")
    
    elif board[0][0] == board[1][1] == board[2][2] != 0:
        checker(winner)

    elif board[2][0] == board[1][1] == board[0][2] != 0:
        checker(winner)

    elif board[0][0] == board[0][1] == board[0][2] != 0:
        checker(winner)

    elif board[1][0] == board[1][1] == board[1][2] != 0:
        checker(winner)

    elif board[2][0] == board[2][1] == board[2][2] != 0:
        checker(winner)

    elif board[0][0] == board[1][0] == board[2][0] != 0:
        checker(winner)

    elif board[0][1] == board[1][1] == board[2][1] != 0:
        checker(winner)

    elif board[0][2] == board[1][2] == board[2][2] != 0:
        checker(winner)

    else:
        pass


def click(x, y):
    global turn, i
    if turn == 0:
        if virtual_board[x][y]:
            pass
        else:
            virtual_board[x][y] = "X"
            turn = 1
        
            button_storage[0][x][y]["text"] = "X"
            button_storage[0][x][y]["fg"] = "white"
            i+=1
            verification_win(virtual_board, turn, i)

    else:
        if virtual_board[x][y]:
            pass
        else:
            virtual_board[x][y] = "O"
            turn = 0

            button_storage[0][x][y]["text"] = "O"
            button_storage[0][x][y]["fg"] = "white"
            i+=1
            verification_win(virtual_board, turn, i)


button_easter.bind(
    "<Button-1>",
    func=lambda rien: messagebox.showinfo(
        "Easter Egg", "Vous avez trouvé le boutton caché o_O"
    ),
)
button_easter.bind(
    "<Enter>", func=lambda rien: button_easter.config(activebackground=main_color)
)


table.pack(expand=1)

# Shower

window.mainloop()
