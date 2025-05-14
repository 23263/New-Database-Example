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

def search_players_by_more_goals_than_response():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    more_goals_than_response = input("How many goals should the player have more than? ")
    sql = "SELECT * FROM Footballer WHERE goals > ? ORDER BY goals ASC"
    cursor.execute(sql, (more_goals_than_response,))
    goals = cursor.fetchall()
    print("Footballer:            Goals:     National team:")
    for footballer in goals:
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
    user_input = input("What would you like to do?\n"
                        "1: Print all footballer data\n"
                        "2: Print all footballers by goals from least to most\n" 
                        "3: print all footballers by goals from most to least\n"
                        "4: Search footballers by nationality\n"
                        "5: Search footballer by club name\n"
                        "6: Search for team name by home ground\n"
                        "7: Search for home ground by team name\n"
                        "8: Stop\n")
    if user_input ==  "1":
        print_all_footballer()
    elif user_input == "2":
        print_all_footballer_by_goals_asc()
    elif user_input == "3":
        print_all_footballer_by_goals_desc()
    elif user_input == "4":
        search_players_by_more_goals_than_response()
    elif user_input == "5":
        search_footballers_by_nationality()
    elif user_input == "6":
        search_footballers_by_club_name()
    elif user_input == "7":
        search_team_name_for_home_ground()
    elif user_input == "8":
        search_home_ground_for_team_name()
    elif user_input == "9":
        break
    else: print("That is not an option.")