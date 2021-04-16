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

window = Tk()
main_color = "#0B243B"
version = "1.0.0"

window.configure(bg=main_color)
window.title("Morpion {}".format(version))
window.minsize(500, 500)

# Body

frame_top = Frame(window, bg="#0B0B61")
frame_top.pack(side=TOP, fill="x")

frame_top_title = Label(
    frame_top,
    text="Morpion",
    bd="5",
    relief=SUNKEN,
    font="Verdana 25 bold",
    fg="white",
    bg=main_color,
)
frame_top_title.pack(pady=25)

separator = Frame(frame_top, bg="white", width="450px", height="5px")
separator.pack(pady=25)


frame_middle = Frame(window, bg="red", width=650, height=50)
frame_middle_label_left = Label(frame_middle, text="X : 0", fg="black")
frame_middle_label_left.place(x=50)
frame_middle_label_right = Label(frame_middle, text="O : 0", fg="black")
frame_middle_label_right.place(x=600)
frame_middle.pack()
frame_bottom = Frame(window, bg=main_color)
frame_bottom.pack(side=BOTTOM, fill="x")

table = Frame(window, bg="red")

width_button = 5
height_button = 5
color_button = main_color


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
button_easter.grid(row=2, column=2)

button_storage.append(
    [
        [button_1, button_2, button_3],
        [button_4, button_5, button_6],
        [button_7, button_8, button_9],
    ]
)


score_o = 0
score_x = 0


def checker(c):
    global virtual_board, button_storage, score_o, score_x
    if c == 0:
        print()
        print("O won.")
        virtual_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        score_o = 1
        frame_middle_label_right["text"] = "O : {}".format(score_o)
        for i in range(len(button_storage)):
            for j in range(len(button_storage[i])):
                for k in range(len(button_storage[i][j])):

                    button_storage[i][j][k]["text"] = ""
    elif c == 1:
        print()
        print("X won.")
        virtual_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        score_x = 1
        frame_middle_label_left["text"] = "X : {}".format(score_x)
        for i in range(len(button_storage)):
            for j in range(len(button_storage[i])):
                for k in range(len(button_storage[i][j])):

                    button_storage[i][j][k]["text"] = ""
    else:
        pass


def verification_win(board, winner):
    if board[0][0] == board[1][1] == board[2][2] != 0:
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
    global turn
    if turn == 0:
        virtual_board[x][y] = "X"
        turn = 1

        button_storage[0][x][y]["text"] = "X"
        button_storage[0][x][y]["fg"] = "white"
        verification_win(virtual_board, turn)

    else:
        virtual_board[x][y] = "O"
        turn = 0

        button_storage[0][x][y]["text"] = "O"
        button_storage[0][x][y]["fg"] = "white"
        verification_win(virtual_board, turn)


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
