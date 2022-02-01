import mysql.connector


mydb = mysql.connector.connect(
  host = "localhost",
  user = "username",
  password = "password",
  database = "database_name"
)

mycursor = mydb.cursor()
sql = "INSERT INTO movies (movie_name, year_of_release) VALUES (%s, %s)"
val = ("Lead_actor", "alu arjun")

mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "details inserted")

mydb.close()
