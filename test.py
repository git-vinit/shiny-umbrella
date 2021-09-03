import mysql.connector
mydb= mysql.connecter.connect(
    host="localhost",
    user="root",
    password="yourpassword"
    )
print(mydb)    
