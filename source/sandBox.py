from tkinter import *
from query import Query

class Root:
    def __init__(self):
        self.root=Tk()
        self.root.title =("titre")
        self.root.geometry("900x1130")
        self.root.minsize(480, 360)
        self.root.config(background="white")

        self.compute()

    def compute(self):
        self.display_ligne()

    def a(self, text):
        print(text)

    def display_ligne(self):
        var1= IntVar()
        ligne_of_bus = [('Rouge',), ('Vert',), ('Bleu',), ('Noir',)]
        frame_ligne = Frame(self.root).pack()
        for i in ligne_of_bus:
            Label(frame_ligne, )

Root().root.mainloop()