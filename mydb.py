import mysql.connector

database = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = '29011998'
	)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("All Done")