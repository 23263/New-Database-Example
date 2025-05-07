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
    print(f"Footballer: {footballer[1]} Goals: {footballer[2]} National team: {footballer[3]}")
    db.close

#main code
print_all_footballer