import mysql.connector

class Query():
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="breizhibus")
        self.cursor = self.mydb.cursor()


    def get_all_arrets_lignes(self):
        self.cursor.execute("""SELECT * FROM arrets_lignes""")
        return self.cursor.fetchall()

    def BFS(self, target=19):
        piste = []
        fifo = []
        item = self.get_all_arrets_lignes()
        for i in item:
            if i[1] == target:
                piste.append(i)
        for i in piste:
            for y in item:
                if y[0] == i[0]:
                    fifo.append(y)
        print(fifo)




print(Query().BFS())
