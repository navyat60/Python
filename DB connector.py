import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Navya@1204"
)

mycur = conn.cursor()

if(mycur):
    print("Success")
else:
    print("Failed")


query="create database abc"
mycur.execute(query)

