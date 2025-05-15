#docstring - Ben Jorgensen - footballer database application
#imports
import sqlite3

#constants and variables
DATABASE = "footballer.db"

#functions
def print_all_footballer():
    #print all footballer data
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
    #print all footballer data by goals from least to most
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
    #print all footballers by goals from most to least
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
    try:
        #print all footballer footballer data with more goals than response
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        more_goals_than_response = int(input("How many goals should the player have more than? "))
        sql = "SELECT * FROM Footballer WHERE goals > ? ORDER BY goals ASC"
        cursor.execute(sql, (more_goals_than_response,))
        goals = cursor.fetchall()
        print("Footballer:            Goals:     National team:")
        for footballer in goals:
            print(f"{footballer[1] :<22} {footballer[2]:<10} {footballer[3]}")
        db.close()
    except ValueError:
        print("That is not a number")

def search_footballers_by_nationality():
    #list of nationalities
    nationalities = {"Argentina", "Netherlands", "Egypt", "England", "Norway", "Uruguay", "Brazil", "Spain", "France", "Italy", "Germany", "Switzerland", "Georgia"}
    #print all footballer data with searched nationality
    try:
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        nationality_response = input("What nationality? ")
        nationality_response_title = nationality_response.title()
        if nationality_response_title not in nationalities:
            raise ValueError
        sql = "SELECT * FROM footballer WHERE nationality = ?;" 
        cursor.execute(sql, (nationality_response_title,))
        footballer = cursor.fetchall()
        print("Footballer:            Goals:     National team:")
        for footballer in footballer:
            print(f"{footballer[1] :<22} {footballer[2]:<10} {footballer[3]}")
        db.close()
    except ValueError as Error:
        print("That is not a country")
        

def search_footballers_by_club_name():
    #list of clubs
    clubs = "Liverpool", "Arsenal", "Real Madrid", "Barcelona", "Inter Milan", "Bayern Munich", "Bayer Leverkusen", "Paris Saint Germain"
    #print all footballer data with searched club
    try:
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        play_club_response = input("What club do they play for? ")
        play_club_response_title = play_club_response.title()
        if play_club_response_title not in clubs:
            raise ValueError
        sql = "SELECT Footballer.name, Footballer.goals, Footballer.nationality FROM Footballer JOIN Teams ON Footballer.team_id = Teams.team_id WHERE Teams.team_name = ?;" 
        cursor.execute(sql, (play_club_response_title,))
        footballer = cursor.fetchall()
        print("Footballer:            Goals:     National team:")
        for footballer in footballer:
            print(f"{footballer[0] :<22} {footballer[1]:<10} {footballer[2]}")
        db.close()
    except ValueError as Error:
        print("That is not a club name")

def search_team_name_for_home_ground():
    #list of team names
    clubs = "Liverpool", "Arsenal", "Real Madrid", "Barcelona", "Inter Milan", "Bayern Munich", "Bayer Leverkusen", "Paris Saint Germain"
    #search for a club with the home ground name
    try:
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        club_response = input("What clubs home ground are you looking for? ")
        club_response_title = club_response.title()
        if club_response_title not in clubs:
            raise ValueError
        sql = "SELECT * FROM Teams WHERE team_name = ?;" 
        cursor.execute(sql, (club_response_title,))
        home_ground = cursor.fetchall()
        print("Club team:            Home ground:")
        for footballer in home_ground:
            print(f"{footballer[1] :<21} {footballer[2]}")
    except ValueError as Errors:
        print("That is not a club name")

def search_home_ground_for_team_name():
    #list of home ground names
    home_grounds = "Anfield", "Emirates Stadium", "Santiago Bernabeu Stadium", "Estadi Olimpic Lluis Companys", "San Siro", "Allianz Arena", "Bay Arena", "Parc Des Princes"
    #search for a home ground with the club name
    try:
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        home_ground_response = input("What home ground does the club your looking for play at? ")
        home_ground_response_title = home_ground_response.title()
        if home_ground_response_title not in home_grounds:
            raise ValueError
        sql = "SELECT * FROM Teams WHERE home_ground = ?;" 
        cursor.execute(sql, (home_ground_response_title,))
        club = cursor.fetchall()
        print("Home Ground:            Club:")
        for footballer in club:
            print(f"{footballer[2] :<23} {footballer[1]}")
    except ValueError as Errors:
        print("That is not a home ground")


#main code
while True: 
    user_input = input("What would you like to do?\n"
                        "1: Print all footballer data\n"
                        "2: Print all footballers by goals from least to most\n" 
                        "3: Print all footballers by goals from most to least\n"
                        "4: Print all footballers with more goals than response\n"
                        "5: Search footballers by nationality\n"
                        "6: Search footballer by club name\n"
                        "7: Search for team name by home ground\n"
                        "8: Search for home ground by team name\n"
                        "9: Stop\n")
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