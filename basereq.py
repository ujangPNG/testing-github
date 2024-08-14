import mysql.connector as sqls

try:
    ko=sqls.Connect(host="127.0.0.1",user="root",password="",port=3306)
    print(ko.is_connected)
except (Exception):
    print(Exception +" bwop")

cur=ko.cursor()

cur.execute(operation="create database if not exists PPLG1")