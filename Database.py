import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="navya@1204"
)

mycurs = mydb.cursor()
mycurs.execute("SHOW DATABASES")

for db in mycurs:
    print(db)