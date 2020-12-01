from tkinter import *
from query import Query

class Root:
    def __init__(self):
        self.root=Tk()
        self.root.title =("titre")
        self.root.geometry("900x1130")
        self.root.minsize(480, 360)
        self.root.config(background="white")

    def compute(self):
        self.header("#44d9e6", "GESTION\nINFORMATISEE\nDES LIGNES BREIZHIBUS")
        self.area_square()
        Root().root.mainloop()
    
    def header(self, color, text):
        frame_header = Frame(self.root,height=200, bg = color)
        label_header = Label(frame_header, bg=color, fg='gray',text=text, justify=LEFT, font=(None,40), height=5).pack(side=LEFT)
        frame_header.pack(fill=X)

    def _square(self, frame_parent):
        return Frame(frame_parent, height=300, width=300, bg="white",highlightbackground="black",highlightthickness=5)
        
    
    def area_square(self):

#Premier ligne
        ligne_1 = Frame(self.root)

        row_1 = self._square(ligne_1)
        Widget().display_ligne_of_bus(row_1)
        row_1.pack(side="left", fill='both')

        row_2 = self._square(ligne_1)
        Widget().widget_input(row_2)
        row_2.pack(side="left", fill='both')

        row_3 = self._square(ligne_1)
        Widget().formulaire(row_3)
        row_3.pack(side="left", fill='both')
#Seconde ligne
        ligne_2 = Frame(self.root)
        row_1 = self._square(ligne_2)
        row_1.pack(side="left", fill='both')
        row_2 = self._square(ligne_2)
        row_2.pack(side="left", fill='both')
        row_3 = self._square(ligne_2)
        row_3.pack(side="left", fill='both')
#Troisieme ligne
        ligne_3 = Frame(self.root)
        row_1 = self._square(ligne_3)
        row_1.pack(side="left", fill='both')
        row_2 = self._square(ligne_3)
        row_2.pack(side="left", fill='both')
        row_3 = self._square(ligne_3)
        row_3.pack(side="left", fill='both')

        ligne_1.pack()
        ligne_2.pack()
        ligne_3.pack()

class Widget(Root):

    def display_ligne_of_bus(self, ligne):
        text = Query().get_all_lignes()
        Label(ligne, text="lignes: ").pack(side="left")
        for i in text:
            Label(ligne, text=i).pack(side="left")

    def _display_arret(self, text, frame):
        frame_label = Frame(frame)
        arret_ligne = Query().get_arrets_for_ligne(text)
        Label(frame_label, text= "LIGNES: ").pack()
        for i in arret_ligne["lignes"]:
            Label(frame_label, text=i).pack()

        Label(frame_label, text="ARRETS:").pack()
        for i in arret_ligne["arrets"]:
            Label(frame_label, text=i).pack()
        frame_label.pack()

    def widget_input(self, ligne):
        entry1 = Entry(ligne)
        entry1.pack()
        Button(ligne, text="click me",  command=lambda: self._display_arret(entry1.get(), ligne)).pack()

    def formulaire(self, ligne):
        entry1 = Entry(ligne).pack()
        entry2 = Entry(ligne).pack()
        Button(ligne, text="ajouter",  command=lambda: self.add_bus(entry1.get(), entry2.get())).pack()
        Button(ligne, text="suprimer",  command=lambda: self._display_arret(entry1.get(), ligne)).pack()
        Button(ligne, text="modifier",  command=lambda: self._display_arret(entry1.get(), ligne)).pack()
    
    def add_bus(self, ligne, bus):
        Query().add_bus(bus,ligne)

Root().compute()

        

