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

def search_home_ground_for_team_name():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    home_ground_club_response = input("What home ground does the club your looking for play at? ")
    home_ground_club_response_title = home_ground_club_response.title()
    sql = "SELECT * FROM Teams WHERE home_ground = ?;" 
    cursor.execute(sql, (home_ground_club_response_title,))
    club = cursor.fetchall()
    print("Home Ground:            Club:")
    for footballer in club:
        print(f"{footballer[2] :<23} {footballer[1]}")

#main code
while True: 
    user_input = input("What would you like to do? \nPress 1 for print all footballer data \nprint all footballers by goals from least to most \n3 for print all footballers by goals from most to least \n4 for search footballers by nationality \n5 for search footballer by club name \n6 for search for team name by home ground \n7 for search for home ground by team name8 to stop.")
    if user_input ==  "1":
        print_all_footballer()
    elif user_input == "2":
        print_all_footballer_by_goals_asc()
    elif user_input == "3":
        print_all_footballer_by_goals_desc()
    elif user_input == "4":
        search_footballers_by_nationality()
    elif user_input == "5":
        search_footballers_by_club_name()
    elif user_input == "6":
        search_team_name_for_home_ground()
    elif user_input == "7":
        search_home_ground_for_team_name()
    elif user_input == "8":
        break
    else: print("That is not an option.")