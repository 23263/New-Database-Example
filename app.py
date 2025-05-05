import sqlite3

db = sqlite3.connect("footballer.db")
cursor = db.cursor()
sql = "SELECT * FROM footballer;"
cursor.execute(sql)
results = cursor.fetchall()
print(results)


db.close