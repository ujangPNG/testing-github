import mysql.connector as SQL
import pandas as pd

class Main:
    def __init__(self):
        self.HOSTNAME="127.0.0.1"
        self.USERNAME="root"
        self.CODE=""
        self.MyConnection=SQL.connect(host=self.HOSTNAME, user=self.USERNAME, password=self.CODE)

    def MyDatabaseConnection(self,db):
        Conn=SQL.Connect(host=self.HOSTNAME, user=self.USERNAME, password=self.CODE, database=db)
        return Conn

    def dml(self, conns, query):
        cursor = conns.cursor()
        cursor.execute(query)
        conns.commit()

    def view(self, connection):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM siswa")
        data = cursor.fetchall()
        Arr = []
        for d in data:
            Arr.append(d)
        print(pd.DataFrame(data=Arr,columns=["id","nama"]))

if(__name__):
    ex = Main()
    cursor = ex.MyConnection.cursor()
    sqlcommand = "Show Databases"
    cursor.execute(sqlcommand)

    for i in cursor:
        print(list(i))

    db = str(input("Select db: "))
    mydbcon = ex.MyDatabaseConnection(db)
    cursor2 = mydbcon.cursor()
    cursor2.execute("Show Tables")

    for j in cursor2:
        print(list(j))

    commandquery = str(input("Query: "))
    ex.dml(mydbcon, commandquery)
    ex.view(mydbcon)
    #as