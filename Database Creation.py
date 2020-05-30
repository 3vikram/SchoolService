import mysql.connector

mydb = mysql.connector.connect(
  host="myrds.cos1fmkyxsdy.ap-south-1.rds.amazonaws.com",
  user="vikram",
  passwd="Kuttyseed02022019"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE School")
