import xlrd
from xlwt import Workbook, Formula
from Tkinter import *
from tkMessageBox import *
import pandas as pd
import numpy as np

#chemin par default a modifier pour chez vous
path = r"/home/jeremie/log.xls"

#initialise notre fenetre principale tkinter
fenetre = Tk()

#On veut juste donner la possibilite a l'utilisateur de choisir ou enregistrer son fichier xls
def NewPath():
    top = Toplevel(fenetre)
    Path = Label(top, text = 'Path : (ex : r"/home/jeremie/log.xls")')
    Path.grid(column=0, row=0, sticky='w')
    Path = StringVar()
    Champ3 = Entry(top, textvariable= Path, width=31)
    Champ3.grid(sticky='sw', columnspan=2)
    path = Path.get()
    quit = Button(top, text="envoyer", command = top.destroy)
    quit.grid ()


#Cree menu tkinter
menu = Menu(fenetre)
fenetre.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="Options", menu=filemenu)
filemenu.add_command(label="Path", command=NewPath)


champ_label = Label(fenetre, text="Fiche d'utilisation de l'ordinateur")

#demande avec un pop up si l'utilisateur a bien rempli le formulaire
def callback():
    if askyesno('', 'Avez vous rempli le formulaire ?'):
        fenetre.destroy()
    else:
        showinfo('', 'Remplissez le formulaire')

#On cree le champ de saisie Nom 
Nom = Label(fenetre, text = 'Nom : ')
Nom.grid(column=0, row=0, sticky='w')
Nom = StringVar()
Champ = Entry(fenetre, textvariable= Nom, width=31)
Champ.grid(column=1, row=0, sticky='sw', columnspan=2, padx=10)

#On cree le champ de saisie Prenom 
Prenom = Label(fenetre, text = 'Prenom : ',)
Prenom.grid(column=0, row=1,sticky='w',pady=2)
Prenom=StringVar()
Champ2 = Entry(fenetre, textvariable= Prenom, width=31)
Champ2.grid(column=1, row=1,columnspan=2)


#la fonction permettant d'ecrire dans le fichier xls
#on utilise la librairie panda pour recuperer les donnees du fichier xls, on crer ensuite un dataframe avec le nom/prenom rentre
#par l'utilisateur, et on concatene le dataframe du xls et celui nom/prenom. On ecrase ensuite le fichier xls avec le new dataframe
def envoyer():
    df = pd.read_excel(path,encoding='utf-8') 
    data = pd.Series([Nom.get()])
    data2 = pd.Series([Prenom.get()])
    df1 = pd.DataFrame({'Nom':data, 'Prenom':data2})
    df2 = pd.concat([df, df1])
    print(df2)
    writer = pd.ExcelWriter('log.xls')
    df2.to_excel(writer, sheet_name='Sheet1')
    writer.save()

 #On cree les boutons interactifs
Fermer = Button(fenetre, text="Fermer", command=callback, pady = 2)
Fermer.grid (column=1, row=11,sticky='sw', pady=20)
Envoyer = Button(fenetre, text="Envoyer", command=envoyer, pady = 2)
Envoyer.grid (column=2, row=11,sticky='sw',pady=20)



fenetre.mainloop()
