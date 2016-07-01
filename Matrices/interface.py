# -*- coding: utf-8 -*-


def nouvelleMatrice(fen, label, entryMsg):
        n = int(entryMsg.get())
        label.grid(row=1, column=1)
        label.pack()
        entryMsg.grid(row=2, column=1)
        label.pack()
        for ligne in range(3,n):
            for colonne in range(n):
                    Entry(fen).grid(row=ligne, column=colonne)


def SysLineaire():
	fen = Tk()
	fen.title('Systeme Lineaire')
	
	labelMsg = Label(fen, text="Donnez la taille de la matrice carré A")
	labelMsg.pack()

	entryMsg = Entry(fen)
	entryMsg.pack()

	buttonVal = Button(fen, text="Valider",command=lambda: nouvelleMatrice(fen,labelMsg,entryMsg)).pack()

	fen.mainloop();

 
from tkinter import * 

fenetre = Tk()

label = Label(fenetre, text="Veuillez faire votre choix parmi les options ci-dessous ")
label.pack()

buttonSL = Button(fenetre, text="Systeme Lineaire", command=SysLineaire)
buttonSL.pack()

fenetre.mainloop()
