import mysql.connector as SQL

conn=SQL.connect(host="127.0.0.1",user="root",password="",port=3306)
cursor=conn.cursor()
sqlquery="show databases"
cursor.execute(sqlquery)
print(cursor.fetchall())