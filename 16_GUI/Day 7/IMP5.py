import mysql.connector
con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1309"
)
cursor=con.cursor()
try:
    cursor.execute("create database python_db")
    db=cursor.execute("show database")

except:
    con.rollback()
    for i in cursor:
        print(i)

con.close()
print(cursor)
