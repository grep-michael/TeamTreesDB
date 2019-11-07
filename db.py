import sqlite3

#run this file to setup db
if __name__ == '__main__':
	conn = sqlite3.connect("donators.db")
	c = conn.cursor()
	c.execute("CREATE TABLE donors (\
		name text,\
		message text,\
		amount integer,\
		date date,\
		id text,\
		PRIMARY KEY(id)\
		)")
	conn.close()
	

class database():
	def __init__(self,name):
		self.conn = sqlite3.connect(name)
		self.c = self.conn.cursor()

	def insert(self, name, message,ammount,date,id):
		self.c.execute("INSERT INTO donors VALUES (?,?,?,?,?)",(name,message,ammount,date,id))
		self.commit()

	def commit(self):
		self.conn.commit()

	def close(self):
		self.conn.close()