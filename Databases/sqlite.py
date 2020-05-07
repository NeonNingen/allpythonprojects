import sqlite3

connection = sqlite3.connect('main.db')
cursor = connection.cursor()

def create_table():
    cursor.execute(
    	"CREATE TABLE IF NOT EXISTS AccountInfo(Login TEXT, Password TEXT, Website TEXT)")

def data_entry():
	cursor.execute("INSERT INTO AccountInfo VALUES('','','')")

	connection.commit()
	cursor.close()
	connection.close()
    
create_table()
data_entry()