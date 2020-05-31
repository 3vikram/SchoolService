import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="vikram",
  passwd="Kuttyseed02022019"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE School")
