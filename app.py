#docstring - Ben Jorgensen - footballer database application
#imports
import sqlite3

#constants and variables
DATABASE = "footballer.db"

#functions
def print_all_footballer():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM footballer;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    db.close

#main code
for footballer in results
    print(f"Footballer name: ")