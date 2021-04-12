from tkinter import *

#fenetre
window = Tk()

#grille du morpion 
grid_canvas = Frame(window)
grid_canvas.grid(row=3, column=1, rowspan=3, columnspan=3)

canvas = Canvas(grid_canvas, width=600, height=600, bg="black")
canvas.grid(row=0,column=0)


#fonctions
def circle(x1,y1,x2,y2):
    global canvas, canvas
    canvas.create_oval(x1, y1, x2, y2, outline="red", width=10)

def cross(x1,y1,x2,y2):
    global canvas, canvas
    canvas.create_line(x1, y1, x2, y2, fill="blue", width=10)
    canvas.create_line(x1, y2, x2, y1, fill="blue", width=10)

def turn_manager():
    global turn, turn
    turn += 1
    if turn%2 == 0:
        player_turn.configure(text="C'est à Joueur 1")
    else:
        player_turn.configure(text="C'est à Joueur 2")

def game_manager(x1,y1,x2,y2):
    global turn, turn
    turn_manager()
    if turn != 0:
        if turn%2 == 0:
            cross(x1,y1,x2,y2)
        else:
            circle(x1,y1,x2,y2)


#informations
window.title("Morpion")
turn = 0

#informations en jeu
player_turn = Label(window, text="C'est à Joueur 1", font=("Helvetica", 10))
player_turn.grid(row=0, column=2)

player1 = Label(window, text="Joueur 1", font=("Helvetica", 30))
player1.grid(row=0, column=1)

player2 = Label(window, text="Joueur 2", font=("Helvetica", 30))
player2.grid(row=0, column=3)

symbol1 = Label(window, text="O", font=("Helvetica", 30))
symbol1.grid(row=1, column=1)

symbol2 = Label(window, text="X", font=("Helvetica", 30))
symbol2.grid(row=1, column=3)

a = Label(window, text="A", font=("Helvetica", 48))
a.grid(row=2, column=1)

b = Label(window, text="B", font=("Helvetica", 48))
b.grid(row=2, column=2)

c = Label(window, text="C", font=("Helvetica", 48))
c.grid(row=2, column=3)

one = Label(window, text="1", font=("Helvetica", 48))
one.grid(row=3, column=0)

two = Label(window, text="2", font=("Helvetica", 48))
two.grid(row=4, column=0)

three = Label(window, text="3", font=("Helvetica", 48))
three.grid(row=5, column=0)

#grille pour placer nos cercles et croix
grid_button = Frame(window)
grid_button.grid(row=1, column=2)

button1 = Button(grid_button, text="Placer un jeton en A1",command=game_manager(10, 10, 190, 190))
button1.grid(row=0,column=0)

button2 = Button(grid_button, text="Placer un jeton en A2",command=game_manager(10, 210, 190, 390))
button2.grid(row=1,column=0)

button3 = Button(grid_button, text="Placer un jeton en A3",command=game_manager(10, 410, 190, 590))
button3.grid(row=2,column=0)

button4 = Button(grid_button, text="Placer un jeton en B1",command=game_manager(210, 10, 390, 190))
button4.grid(row=0,column=1)

button5 = Button(grid_button, text="Placer un jeton en B2",command=game_manager(210, 210, 390, 390))
button5.grid(row=1,column=1)

button6 = Button(grid_button, text="Placer un jeton en B3",command=game_manager(210, 410, 390, 590))
button6.grid(row=2,column=1)

button7 = Button(grid_button, text="Placer un jeton en C1",command=game_manager(410, 10, 590, 190))
button7.grid(row=0,column=2)

button8 = Button(grid_button, text="Placer un jeton en C2",command=game_manager(410, 210, 590, 390))
button8.grid(row=1,column=2)

button9 = Button(grid_button, text="Placer un jeton en C3",command=game_manager(410, 410, 590, 590))
button9.grid(row=2,column=2)

#affichage
window.mainloop()