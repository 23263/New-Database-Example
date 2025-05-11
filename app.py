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
    db.close()

def print_all_footballer_by_goals_asc():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM footballer ORDER BY Goals ASC;"
    cursor.execute(sql)
    footballer = cursor.fetchall()
    print("Footballer:            Goals:     National team:")
    for footballer in footballer:
        print(f"{footballer[1] :<22} {footballer[2]:<10} {footballer[3]}")
    db.close()

def print_all_footballer_by_goals_desc():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM footballer ORDER BY Goals DESC;"
    cursor.execute(sql)
    footballer = cursor.fetchall()
    print("Footballer:            Goals:     National team:")
    for footballer in footballer:
        print(f"{footballer[1] :<22} {footballer[2]:<10} {footballer[3]}")
    db.close()

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
    db.close()

def search_footballers_by_club_name():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    play_club_response = input("What club do they play for? ")
    play_club_response_title = play_club_response.title()
    sql = "SELECT Footballer.name, Footballer.goals, Footballer.nationality FROM Footballer JOIN Teams ON Footballer.team_id = Teams.team_id WHERE Teams.team_name = ?;" 
    cursor.execute(sql, (play_club_response_title,))
    footballer = cursor.fetchall()
    print("Footballer:            Goals:     National team:")
    for footballer in footballer:
     print(f"{footballer[0] :<22} {footballer[1]:<10} {footballer[2]}")
    db.close()

def search_team_name_for_home_ground():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    home_ground_club_response = input("What clubs home ground are you looking for? ")
    home_ground_club_response_title = home_ground_club_response.title()
    sql = "SELECT * FROM Teams WHERE team_name = ?;" 
    cursor.execute(sql, (home_ground_club_response_title,))
    home_ground = cursor.fetchall()
    print("Club team:            Home ground:")
    for footballer in home_ground:
        print(f"{footballer[1] :<21} {footballer[2]}")

#main code
search_team_name_for_home_ground()