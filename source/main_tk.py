from tkinter import *
from tkinter import messagebox
from query import Query
from pygments.lexers import j

class Root:
    def __init__(self):
        self.root=Tk()
        self.root.title =("titre")
        self.root.geometry("1130x1130")
        self.root.minsize(720, 720)
        self.root.config(background="white")

        self.ligne_info = StringVar()
        self.ligne = StringVar()
        self.immatriculation = StringVar()
        self.place = StringVar()
        self.bus = StringVar()
        self.start = StringVar()
        self.end = StringVar()

        self.compute()

    def compute(self):
        self.display_ligne()


    def display_ligne(self):
        photo = PhotoImage(file="/Users/guillaumeverpoest/Desktop/isen-Project/Briefs/Breizhibus/Images/del.png")
        frame = Frame(self.root).grid()
        j=0
        for i in Query().get_info_bus():
            Label(frame, text=i[0], width=30, height=5).grid(column=2, row=j)
            Label(frame, text=i[1], width=30, height=5).grid(column=3, row=j)
            Label(frame, text=i[2], width=30, height=5).grid(column=4, row=j)
            Button(frame, text="Suprimer", bg='gray',width=10, height=5, command=lambda name=i[0]: self.delete_bus(name)).grid(column=5, row=j)
            j+=1
        frame1 = Frame(frame, bg='gray', width=50, height=50).grid(columnspan=10, sticky=W+E)
        j+=1
        Label3 = Label(self.root, text = 'Info sur une ligne : ')
        Label3.grid(column=2, row=j, sticky='w')
        Champ = Entry(self.root, textvariable= self.ligne_info, width=31)
        Champ.focus_set()
        Champ.grid(column=3, row=j, sticky='sw', columnspan=2, padx=10)
        Button (self.root, text="Envoyer", command=lambda: self.compute2(), pady=2).grid(column=4, row=j)

        Frame(frame, bg='gray', width=50, height=50).grid(columnspan=10, sticky=W+E)
        j+=2
        Label1 = Label(self.root, text = 'Numeros du bus : ')
        Label1.grid(column=2, row=j, sticky='w')
        Champ = Entry(self.root, textvariable = self.bus, width=31)
        Champ.focus_set()
        Champ.grid(column=3, row=j, sticky='sw', columnspan=2, padx=10)

        j+=3
        Label1 = Label(self.root, text = 'Nombre de place : ')
        Label1.grid(column=2, row=j, sticky='w')
        Champ = Entry(self.root, textvariable = self.place, width=31)
        Champ.focus_set()
        Champ.grid(column=3, row=j, sticky='sw', columnspan=2, padx=10)

        j+=4
        Label3 = Label(self.root, text = 'Immatriculation : ')
        Label3.grid(column=2, row=j, sticky='w')
        Champ = Entry(self.root, textvariable= self.immatriculation, width=31)
        Champ.focus_set()
        Champ.grid(column=3, row=j, sticky='sw', columnspan=2, padx=10)

        j+=5
        Label4 = Label(self.root, text = 'ligne : ')
        Label4.grid(column=2, row=j, sticky='w')
        Champ = Entry(self.root, textvariable= self.ligne, width=31)
        Champ.focus_set()
        Champ.grid(column=3, row=j, sticky='sw', columnspan=2, padx=10)

        j+=6
        bouton2= Button (self.root, text="Envoyer", command=lambda: self.confirm_formulaire(), pady=2)
        bouton2.grid (column=3, row=j,sticky='sw',pady=20)

        Frame(frame, bg='gray', width=50, height=50).grid(columnspan=10, sticky=W+E)
        j+=7
        Label4 = Label(self.root, text = 'Selection une depart et un arrive')
        Label4.grid(column=2, row=j, sticky='w')
        Champ = Entry(self.root, textvariable= self.start, width=31)
        Champ.focus_set()
        Champ.grid(column=3, row=j, sticky='sw', columnspan=2, padx=10)
        Champ = Entry(self.root, textvariable= self.end, width=31)
        Champ.focus_set()
        Champ.grid(column=4, row=j, sticky='sw', columnspan=2, padx=10)
        bouton2= Button (self.root, text="Envoyer", command=lambda: self.trajet(), pady=2)
        bouton2.grid (column=5, row=j,sticky='sw')


            
    


    def compute2(self):
        a = Query().get_arrets_for_ligne(self.ligne_info.get())
        print(a)
        arrets = a["arrets"]
        bus = a["bus"]
        messagebox.showinfo("Bas", "arrets: %s\n Bus: %s"%(arrets,bus))
    
    def confirm_formulaire(self):
        msg = Query().add_bus(self.ligne.get(), self.bus.get())
        if msg == "le bus existe deja":
            result = messagebox.askquestion("Start a new game", "Le bus existe deja le modifier ?", icon='warning')
            if result == 'yes':
                Query().update_bus(self.bus.get(), "AA", 20, self.ligne.get())
                print(self.ligne.get())
        else:
            messagebox.showinfo("Bas", msg)

    def trajet(self):
        item = Query().get_id_arret(self.start.get(), self.end.get())
        messagebox.showinfo("Bas", "Prenez la ligne %s"%(item))

    def delete_bus(self, bus):
        item = Query().delete_bus(bus)
        messagebox.showinfo("Bas", "%s"%(item))
    


Root().root.mainloop()