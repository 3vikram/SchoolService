import mysql.connector

mydb = mysql.connector.connect(
  host="0.0.0.0",
  user="vikram",
  passwd="Kuttyseed02022019"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE School")
