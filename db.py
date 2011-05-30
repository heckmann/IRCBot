import sqlite3
from os.path import isfile

def connect_DB(database):
	if not isfile(database):
		connection = sqlite3.connect(database)
		cursor = connection.cursor()
		cursor.execute("create table irc (id INTEGER PRIMARY KEY, date TEXT, what TEXT, who TEXT, message TEXT)")
		connection.commit()
		cursor.close()
	
def add(database, order, who, message):
	connection = sqlite3.connect(database)
	cursor = connection.cursor()
	cursor.execute("insert into irc values (NULL, datetime('now', 'localtime'),?,?,?)", (order.decode('utf-8'), who.decode('utf-8'), message.decode('utf-8')))
	connection.commit()
	cursor.close()
	
def saw(database, person):
	connection = sqlite3.connect(database)
	cursor = connection.cursor()
	cursor.execute("select * from irc where who=? ORDER BY date DESC LIMIT 1" , [person.decode('utf-8')])
	connection.commit()
	watched = cursor.fetchall()
	cursor.close()
	if watched:
		return watched[0][1]
	else:
		return "?"