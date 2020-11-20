import mysql.connector


class Query():
    def __init__(self):
        self.mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="breizhibus")
        self.cursor = self.mydb.cursor()

    def get_all_lignes(self):
        self.cursor.execute("""SELECT nom FROM lignes""")
        print(self.cursor.fetchall())

    def get_arrets_for_ligne(self, ligne):
        self.cursor.execute("""SELECT nom  FROM arrets INNER JOIN arrets_lignes ON arrets.id_arret = arrets_lignes.id_arret WHERE id_ligne = (SELECT id_ligne FROM lignes WHERE nom = '%s')"""%(ligne))
        print(self.cursor.fetchall())
        self.cursor.execute("""SELECT numeros FROM bus INNER JOIN lignes ON lignes.id_ligne = bus.id_ligne WHERE lignes.nom = '%s'"""%(ligne))
        print(self.cursor.fetchall())


        
Query().get_arrets_for_ligne('Noir')