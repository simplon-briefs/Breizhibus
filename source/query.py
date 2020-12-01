import mysql.connector


class Query():
    def __init__(self):
        self.mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="breizhibus")
        self.cursor = self.mydb.cursor()

    def get_all_lignes(self):
        self.cursor.execute("""SELECT nom FROM lignes""")
        return(self.cursor.fetchall())

    def get_arrets_for_ligne(self, ligne):
        arret_ligne = {}
        self.cursor.execute("""SELECT nom  FROM arrets INNER JOIN arrets_lignes ON arrets.id_arret = arrets_lignes.id_arret WHERE id_ligne = (SELECT id_ligne FROM lignes WHERE nom = '%s')"""%(ligne))
        arret_ligne["lignes"] = self.cursor.fetchall()
        self.cursor.execute("""SELECT numeros FROM bus INNER JOIN lignes ON lignes.id_ligne = bus.id_ligne WHERE lignes.nom = '%s'"""%(ligne))
        arret_ligne["arrets"] = self.cursor.fetchall()
        return arret_ligne

    def add_bus(self, ligne, bus):
        if self.is_existed_bus(bus):
            if self.is_existed_ligne(ligne):
                self.cursor.execute("""SELECT id_ligne FROM lignes WHERE nom = '%s'"""%(ligne))
                id_ligne = self.cursor.fetchall()[0]
                self.cursor.execute("""INSERT INTO bus(numeros ,id_ligne) VALUES ('%s', %d)"""%(bus, id_ligne[0]))
                self.mydb.commit()
                self.mydb.close()
                return "le bus a bien ete ajouter"
            else:
                return "la ligne existe pas"
        else:
            return "le bus existe deja"
    
    def is_existed_bus(self, bus):
        self.cursor.execute("""SELECT * FROM bus WHERE numeros = '%s'"""%(bus))
        item = self.cursor.fetchall()
        if not item: # le bus existe pas
            return True
        else: # la ligne existe
            return False

    def is_existed_ligne(self, ligne):
        self.cursor.execute("""SELECT * FROM lignes WHERE nom = '%s'"""%(ligne))
        item = self.cursor.fetchall()
        if not item: # la ligne existe pas
            return False
        else: # la ligne existe
            return True

    def delete_bus(self, bus):
        self.cursor.execute("""DELETE FROM bus WHERE numeros = '%s'"""%(bus))

print(Query().add_bus("Noir","BB09"))