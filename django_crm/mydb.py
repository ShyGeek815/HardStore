import mysql.connector

# Подключение к БД
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root1234'
)

# prepare a cursor object
cursoreObject = dataBase.cursor()

# create a database 
cursoreObject.execute("CREATE DATABASE hardstore")

print("Выполнено!")