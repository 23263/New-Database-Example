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
    footballer = cursor.fetchall()
    print("Footballer:            Goals:     National team:")
    for footballer in footballer:
        print(f"{footballer[1] :<22} {footballer[2]:<10} {footballer[3]}")
    db.close

def print_all_footballer_by_goals_asc():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM footballer ORDER BY Goals ASC;"
    cursor.execute(sql)
    footballer = cursor.fetchall()
    print("Footballer:            Goals:     National team:")
    for footballer in footballer:
        print(f"{footballer[1] :<22} {footballer[2]:<10} {footballer[3]}")
    db.close

def print_all_footballer_by_goals_desc():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM footballer ORDER BY Goals DESC;"
    cursor.execute(sql)
    footballer = cursor.fetchall()
    print("Footballer:            Goals:     National team:")
    for footballer in footballer:
        print(f"{footballer[1] :<22} {footballer[2]:<10} {footballer[3]}")
    db.close

def search_footballers_by_nationality():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    nationality_response = input("What nationality? ")
    nationality_response_title = nationality_response.title()
    sql = "SELECT * FROM footballer WHERE nationality = ?;" 
    cursor.execute(sql, (nationality_response_title,))
    footballer = cursor.fetchall()
    print("Footballer:            Goals:     National team:")
    for footballer in footballer:
     print(f"{footballer[1] :<22} {footballer[2]:<10} {footballer[3]}")
    db.close

def search_footballers_by_club_name():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    club_response = input("What club? ")
    club_response_title = club_response.title()
    sql = "SELECT * FROM teams WHERE team_name = ?;" 
    cursor.execute(sql, (club_response_title,))
    team_name = cursor.fetchall()
    print("Footballer:            Goals:     National team:")
    for footballer in team_name:
     print(f"{footballer[1] :<22} {footballer[2]:<10} {footballer[3]}")
    db.close


def test():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    club_response = input("What club? ")
    club_response_title = club_response.title()
    sql = "SELECT * FROM footballers WHERE team_name = ?;" 
    cursor.execute(sql, (club_response_title,))
    team_name = cursor.fetchall()
    print(team_name)
    db.close





#main code
test()