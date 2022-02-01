import mysql.connector as SQLC

DataBase = SQLC.connect(
  host ="server name",
  user ="user name",
  password ="password"
)
Cursor = DataBase.cursor()

Cursor.execute("CREATE DATABASE movies")
print("movies Data base is created")
