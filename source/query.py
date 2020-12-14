import mysql.connector


class Query():
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="breizhibus")
        self.cursor = self.mydb.cursor()

    def get_all_lignes(self):
        self.cursor.execute("""SELECT nom FROM lignes""")
        return(self.cursor.fetchall())

    def get_info_bus(self):
        self.cursor.execute("""SELECT bus.numeros, bus.nombre_place, lignes.nom FROM bus
                            JOIN lignes ON bus.id_ligne = lignes.id_ligne""")
        return(self.cursor.fetchall())

    def get_arrets_for_ligne(self, ligne):
        arret_ligne = {}
        if self._is_existed_ligne(ligne):
            self.cursor.execute("""SELECT nom FROM arrets
                                INNER JOIN arrets_lignes ON arrets.id_arret = arrets_lignes.id_arret 
                                WHERE id_ligne = (SELECT id_ligne FROM lignes WHERE nom = '%s')"""%(ligne))

            arret_ligne["arrets"] = self.cursor.fetchall()
            self.cursor.execute("""SELECT numeros FROM bus
                                INNER JOIN lignes ON lignes.id_ligne = bus.id_ligne 
                                WHERE lignes.nom = '%s'"""%(ligne))

            arret_ligne["bus"] = self.cursor.fetchall()
            return arret_ligne
        else:
            arret_ligne["arrets"] = "la ligne existe pas"
            arret_ligne["bus"] = None
            return arret_ligne


    def add_bus(self, ligne, bus):
        if self._is_existed_bus(bus):
            if self._is_existed_ligne(ligne):
                self.cursor.execute("""SELECT id_ligne FROM lignes WHERE nom = '%s'"""%(ligne))
                id_ligne = self.cursor.fetchall()[0]
                self.cursor.execute("""INSERT INTO bus(numeros ,id_ligne)
                                    VALUES ('%s', %d)"""%(bus, id_ligne[0]))
                self.mydb.commit()
                self.mydb.close()
                return "le bus a bien ete ajouter"
            else:
                return "la ligne existe pas"
        else:
            return "le bus existe deja"
    
    def _is_existed_bus(self, bus):
        self.cursor.execute("""SELECT * FROM bus WHERE numeros = '%s'"""%(bus))
        item = self.cursor.fetchall()
        if not item: # le bus existe pas
            return True
        else: # le bus existe
            return False

    def _is_existed_ligne(self, ligne):
        self.cursor.execute("""SELECT * FROM lignes WHERE nom = '%s'"""%(ligne))
        item = self.cursor.fetchall()
        if not item: # la ligne existe pas
            return False
        else: # la ligne existe
            return True

    def delete_bus(self, bus):
        if not self._is_existed_bus(bus):
            self.cursor.execute("""DELETE FROM bus WHERE numeros = '%s'"""%(bus))
            self.mydb.commit()
            self.mydb.close()
            return "le bus a ete suprimer "
        else:
            return "Le bus n'esite pas"
            

    def update_bus(self, bus, immatriculation, nbr_place, ligne):
        if not self._is_existed_bus(bus):
            if self._is_existed_ligne(ligne):
                self.cursor.execute("""SELECT id_ligne FROM lignes WHERE nom = '%s'"""%(ligne))
                id_ligne = self.cursor.fetchall()[0][0]
                self.cursor.execute("""UPDATE bus SET immatriculation = '%s', nombre_place=%d, id_ligne = %s WHERE numeros = '%s'"""%(immatriculation, nbr_place, id_ligne, bus))
                self.mydb.commit()
                self.mydb.close()
            else:
                return "la ligne n'existe pas"
        else:
            return "le bus n'existe pas"

    def get_id_arret(self, start, end):
        self.cursor.execute("""SELECT id_arret FROM arrets WHERE nom = '%s'"""%(start))
        id_arret = self.cursor.fetchall()[0]
        self.cursor.execute("""SELECT id_ligne, id_arret FROM arrets_lignes WHERE id_arret = %d"""%(id_arret))
        start = (self.cursor.fetchall())
        self.cursor.execute("""SELECT id_arret FROM arrets WHERE nom = '%s'"""%(end))
        id_arret = self.cursor.fetchall()[0]
        self.cursor.execute("""SELECT id_ligne, id_arret FROM arrets_lignes WHERE id_arret = %d"""%(id_arret))
        end = (self.cursor.fetchall())
        a = []
        for i in start:
            for j in end:
                if i[0] == j[0]:
                    a.append(i[0])
        return a