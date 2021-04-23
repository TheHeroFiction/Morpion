"""
Coder par ZedRoff et TheHeroFiction.
Projet NSI.
Version 1.0.0
Tous droits réservés
"""

# Modules

from tkinter import *  # On importe le module tkinter avec tout ses composants

import random  # On importe le module random qui nous permet de rendre aléatoire le début de chaque partie
import time

# Init

window = Tk()  # On instancie une nouvelle fenêtre GUI de tkinter
main_color = "#0B243B"  # Ceci est notre couleur principale du jeu
version = "1.0.0"  # La version du jeu

window.configure(bg=main_color)  # On set le fond d'écran du jeu à la couleur principale de notrejeu
window.title("Morpion {}".format(version))  # On affiche le nom du jeu ainsi que sa version dans l'onglet de la fenêtre
w, h = window.winfo_screenwidth(), window.winfo_screenheight()  # On accède aux informations suivantes : La largeur et longueur maximale supportépar l'écran de l'utilisateur
window.geometry("{}x{}".format(w,h))  # On veut que notre jeu ne soit accessible qu'en plein écran, donc on setsa taille de base à la taille maximale

secondes = 0 #variable qui  servira à mesurer les secondes
minutes = 0 #variable qui  servira à mesurer les minutes
heures = 0 #variable qui  servira à mesurer les heures
#Image
engrenage = PhotoImage(file="engrenage.gif")


# window.minsize(w,h) # Si l'utilisateur veut que la taille de la fenêtre soit bloqué sur lemode plein écran. Problème : Cache un peu le bouton MENU
# Functions

def btn_maker(x, y):  # Cette fonction permet de rendre la création de la grille de bouton plus compact
    return Button(
        table,
        width=width_button,
        height=height_button,
        bg=color_button,
        activebackground=main_color,
        command=lambda: click(x, y),  # Création d'un bouton de notre grille (répété 9 fois)
    )


mode = 0  # Variable qui permet de rendre le bouton menu multitache, il ferme et ouvre le menu


def new_window():  # Fonction qui permet de créer ce nouveau menu et de le supprimer selon le mode
    global mode, menu  # Importation de nos 2 variables clés
    if mode == 0:  # Si la Frame n'est pas présente sur la page
        menu = Frame(window, width=500, height=500, bg="white",borderwidth=10)  # On crée la Frame qui est un carré 500x500
        menu.place(relx=.25, rely=.25)  # On le place au centre de l'écran
        mode = 1  # On déclare que la Frame est présente sur la page
    else:  # Si la Frame est présente sur la page
        menu.destroy()  # On la supprime
        mode = 0  # On déclare que la Framen'est plus présente sur la page


score_o = 0  # Le score du joueur 2
score_x = 0  # Le score du joueur 1

i = 0  # Cette variable permet de déterminer si il y a match nul ou non


def reset():  # Partie assez redondante du code, qui a donc été transformé en fonction, permet de clear le tableau de jeu après victore ou nulle.
    global button_storage  # Importation du tableau qui stock l'ensemble des boutons
    for j in range(len(button_storage[0])):  # # On boucle sur la première partie du tableau dimensionnel
        for k in range(len(button_storage[0][j])):  # Sur la deuxième
            button_storage[0][j][k]["text"] = ""  # Pour le bouton en question, son texte s'actualise sur "" (rien)


def winner(sign):  # Fonction qui incrémente les points, les affiche, actualise les 2 tableaux de jeu
    global score_o, score_x, virtual_board, i  # Importation des variables clés
    frame_middle_label_center["text"] = "{} a gagné.".format(sign)  # On affiche qui a gagné
    virtual_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # On actualise le tableau de jeu virtuelk
    if sign == "O":  # Si c'est le joueur 2 qui a gagné
        score_o += 1  # On incrémente le score de O
        frame_middle_label_right["text"] = "O : {}".format(score_o)  # On affiche ses points
    else:
        score_x += 1  # On incrémente le score de X
        frame_middle_label_left["text"] = "X : {}".format(score_x)  # On incrémente ses points
    reset()  # On clear le tableau de jeu
    i = 0  # On met a 0 le compteur du match nul


def checker(
        c):  # Fonction qui permet d'annoncer le vainqueur, d'incrémenter le score de ce dernier et d'actualiser le tableau virtuel
    global virtual_board, i  # Importation des variables clés
    if c == 0:  # Si c'est le joueur 2 qui gagne la partie
        winner("O")  # On appelle la fonction winner
    elif c == 1:  # Si c'est le joueur 1 qui gagne la partie
        winner("X")  # On appelle la fonction winner
    elif c == "None":  # Si c'est le match nul qui est engendré
        print()
        frame_middle_label_center["text"] = "Match nul"
        virtual_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # On actualise le tableau virtuel
        reset()  # On reset le tableau de jeu
        i = 0  # Reset du draw


def verification_win(board, winner_sign):  # Fonction qui vérifie si un joueur a gagné
    global i
    # Vérification du match nul
    if i == 9:  # 9 cases remplis
        checker("None")
    elif board[0][0] == board[1][1] == board[2][2] != 0:  # Diagonale partant de en haut a gauche à en bas a droite
        checker(winner_sign)
    elif board[2][0] == board[1][1] == board[0][2] != 0:  # Diagonale partant de en bas a gauche a en haut a droite
        checker(winner_sign)
    elif board[0][0] == board[0][1] == board[0][2] != 0:  # Ligne du haut
        checker(winner_sign)
    elif board[1][0] == board[1][1] == board[1][2] != 0:  # Ligne du milieu
        checker(winner_sign)
    elif board[2][0] == board[2][1] == board[2][2] != 0:  # Ligne du bas
        checker(winner_sign)
    elif board[0][0] == board[1][0] == board[2][0] != 0:  # Colonne de gauche
        checker(winner_sign)
    elif board[0][1] == board[1][1] == board[2][1] != 0:  # Colonne du milieu
        checker(winner_sign)
    elif board[0][2] == board[1][2] == board[2][2] != 0:  # Colonne de droite
        checker(winner_sign)

turn = random.randint(0, 1)  # On choisit ici qui sera le premier a jouer

def poser(sign, x, y):  # Fonction qui permet de placer les jetons sur les 2 tableaux (virtuels et celui des bouttons)
    global turn, i  # Importation du tour et de la variable du match nul
    if virtual_board[x][y]:  # Si la case est déjà prise
        pass  # On ne fait rien
    else:
        virtual_board[x][y] = sign  # On place le jeton sur la case demandé (sur le tableau virtuel)
        if turn == 0:  # Si c'est au tour de X
            turn = 1  # On bascule le tour vers O
        else:  # Sinon (si c'est au tour de O)
            turn = 0  # On bascule ce dernier vers X
        button_storage[0][x][y]["text"] = sign  # On écrit le jeton sur le boutton demandé
        button_storage[0][x][y][
            "fg"] = "white"  # On lui donne une couleure blanche (quand un texte est nouvellement ajouté sur tkinter, il faut lui donné une nouvelle couleure).
        i += 1  # On incrémente la variable du match nul de 1
        verification_win(virtual_board, turn)  # On appelle la fonction qui vérifie si il y a un gagnant ou non a chaque clique sur un boutton non prit


def click(x, y):  # Fonction qui gère le clique en prennant 2 paramètres X et Y, étant des coordonnées
    global turn  # Importation du tour
    if turn == 0:  # Si c'est au tour de X
        poser("X", x, y)  # On appelle la fonction poser et on lui passe les arguments X car c'est le tour du joueur 1, ainsi que les coordonnées du boutton pressé
    else:  # Sinon (si c'est le tour de O)
        poser("O", x, y)  # On appelle la fonction poser et on lui passe les arguments O car c'est le tour du joueur 2, ainsi que les coordonnées du boutton pressé

import threading

def timer(): #Fonction qui génère un timer
    global secondes, minutes, heures

    secondes += 1
    if secondes == 60:
        secondes = 0
        minutes += 1
    if minutes == 60:
        minutes = 0
        heures += 1
    
    time_spent["text"] = heures,":",minutes,":",secondes
    
    t = threading.Timer(1,timer)
    t.start()       

    
    

# Body

frame_top = Frame(window, bg="#D65A5A")  # On crée le bloc du haut
frame_top.pack(side=TOP, fill="x")  # On place ce bloc et on lui demande de prendre toute la largeur disponible
frame_top_title = Label(
    frame_top,
    text="Morpion",
    bd="5",
    relief=GROOVE,
    font="Verdana 25 bold",
    fg="white",
    bg=main_color,
)  # On crée un titre qui sera le titre de notre jeu "Morpion" on le place au center

time_frame = Frame(window, height=50, width=300)
time_spent = Label(time_frame,text= "00:00:00")
time_spent.pack()
time_frame.pack(side= TOP)
timer()
frame_top_title.pack(pady=25)  # On place ce titre avec un espacement par rapport au haut pour éviter qu'il soit coller

separator = Frame(frame_top, bg="white", width="450px",height="5px")  # On crée un sort de hr en html, un séprateur qui permet de séparé le bloc du haut du bloc du milieu
separator.pack(pady=25)  # On le place et le sépare de la même façon que le frame_top_title

frame_middle = Frame(window, bg="#6E83DD", width=650,height=50)  # On crée le Frame du milieu qui contiendra lesscores ainsi que celui qui a gagné
frame_middle_label_left = Label(frame_middle, text="X : 0", fg="white", font="Helvetica 15 bold",bg=main_color)  # Score de X
frame_middle_label_left.place(anchor="e", relx=.1, rely=.5)  # Pmacement du score de X a gauche
frame_middle_label_center = Label(frame_middle, text="test", fg="white", font="Helvetica 15 bold",bg=main_color)  # Vainqueur
frame_middle_label_center.place(anchor="c", relx=.5, rely=.5)  # Placement de la personne qui a gagné au centre
frame_middle_label_right = Label(frame_middle, text="O : 0", fg="white", font="Helvetica 15 bold",bg=main_color)  # Score de O
frame_middle_label_right.place(anchor="w", relx=.9, rely=.5)  # Placement du score de O a droite
frame_middle.pack(pady=50)  # On affiche la Frame du milieu
frame_bottom = Frame(window,bg=main_color)  # On crée la Framedu bas qui contiendra le menu ainsi que la grille du morpion
frame_bottom.pack(side=BOTTOM, fill="x")  # La frame prend toute la largeur disponible

table = Frame(window, bg="#F37552", relief=SUNKEN, borderwidth=10,height=600, width=600)  # Grille du morpion


# On peut faire varier la longueur et largeur du boutton ainsi que sa couleur
width_button = 15
height_button = 10
color_button = "#2E2E2E"

virtual_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Tableau de jeu virtuel pour faire les vérifications en back

button_storage = []  # Pour stocker les bouttons afn de boucler dessus pour les modifier un a un

# Création des bouttons
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
    btn_maker(0, 0),
    btn_maker(0, 1),
    btn_maker(0, 2),
    btn_maker(1, 0),
    btn_maker(1, 1),
    btn_maker(1, 2),
    btn_maker(2, 0),
    btn_maker(2, 1),
    btn_maker(2, 2),
    Button(
        frame_bottom, width=1, height=1, bg=color_button, highlightthickness=0, bd=0
    ),
)
# Placement des bouttons dans la frame "table"
button_1.grid(row=0, column=0)
button_2.grid(row=0, column=1)
button_3.grid(row=0, column=2)
button_4.grid(row=1, column=0, pady=5)  # Pour le quadrillage
button_5.grid(row=1, column=1)
button_6.grid(row=1, column=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1, padx=5)  # Pour le quadrillage
button_9.grid(row=2, column=2)

button_menu = Button(window,  image=engrenage, command=new_window, borderwidth=0)  # Le boutton du menu
button_menu.place(anchor="e", relx=.9, rely=.9)  # Placer en bas a droite de l'écran

button_storage.append(
    [
        [button_1, button_2, button_3],
        [button_4, button_5, button_6],
        [button_7, button_8, button_9],
    ]
)  # On rempli le tableau avec l'ensemble des bouttons crée

button_easter.bind(
    "<Button-1>",
    func=lambda rien: messagebox.showinfo(
        "Easter Egg", "Vous avez trouvé le boutton caché o_O"
    ),
)  # Boutton easter egg qui est en bas a gauche de l'écran (action lors du clique)
button_easter.bind(
    "<Enter>", func=lambda rien: button_easter.config(activebackground=main_color)
)  # Pour remettre la couleur de base a l'entrée et a la sortie pour le garder caché

table.pack()  # On affiche le tableau de jeu

# Shower

window.mainloop()  # On affiche la fenêtre (instancie en l'occurence).
