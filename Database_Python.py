# Database_Python.py
# This program is a command line interface for a database of game franchises. It allows the user to view information about different game franchises, including the title, main character, genre, release year, publisher, franchise, and original creator. The user can filter the information by franchise, game, main character, genre, release year, and publisher.
# Variable
import sqlite3 # Import sqlite3 to connect to database
import random 
import time 
import itertools
import threading
import sys 
DATABASE = 'Game_Franchise.db' # Database Name
space = " " # Variable for UI to make space between text
UnderScore = "_" # Variable for UI to make underscore between text

def Load(): # Load Animation
    done = False # Variable to control the loading animation
    if Skip_Loading == True: # Debug skip loading animation
        done = True
    else:
        def animation(): # Loading Animation Function
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\rloading ' + c) 
                sys.stdout.flush()
                time.sleep(0.1)
        if Skip_Loading == False:
            t = threading.Thread(target=animation)
            t.start()
            time.sleep(random.randint(1, 3))
            done = True
            sys.stdout.write('\r')
            sys.stdout.flush()

def Security(): # Security Check
    Username = "Unknown" # Default Username
    Password = "idk" # Default Password
    if Skip_Security_Check == True: # debug skip security check
        return Username # Return default Username
    else: # If not skip security check, ask for username and password
        print("Input your Username")
        Input_Username = input("Username: ")
        Username = Input_Username
        print("Password hint: Acronym for I don't Know") # Hint for password
        while True: # While True Loop to ask for Password
            try: # Try Except to catch error or invalid input
                 Input_Password = input("Password: ")
                 if Input_Password.lower() != Password:
                     raise # Raise error to ask for input again until user input correct password
                 else:
                     return Username
            except: #   If input is invalid or error, print Error
                print('Invalid Input / Incorrect Password')
   
def Return_Menu(): # Quick Return To Menu Function
        while True: # While True Loop to ask for Return to Menu
            try: # Try Except to catch error or invalid input
                 Question = input("Return To Menu? / Y?\n") # Ask to Return to Menu
                 if Question.lower() != "y": # If input is not y,
                     raise # Raise error to ask for input again until user input y
                 elif Question.lower() == "y": # If input is y, return to Menu
                     Menu(Username) # Return to Menu
            except: # If input is invalid or error, print Error
                print("Error")

def Print_All(): #Command 1
    with sqlite3.connect(DATABASE) as db: # Connect to Database
        cursor = db.cursor() # Create Cursor
        SQL_Code_Print_All = """
SELECT 
Game.Title,
Main_Character.Main_Character_Name,
Genre.Genre,
Game.Release_Year,
Publisher.Publisher,
Franchise.Franchise,
Franchise.Original_Creator

FROM Game

JOIN Genre_Bridge on Genre_Bridge.Game_ID = Game.Game_ID
JOIN Genre on Genre.Genre_ID = Genre_Bridge.Genre_ID

JOIN Main_Character_Bridge on Main_character_bridge.Game_ID = game.Game_ID
JOIN Main_Character on Main_character.Main_Character_ID = Main_character_bridge.Main_Character_ID

Join Franchise on Game.Franchise_ID = Franchise.Franchise_ID
Join Publisher on Franchise.Publisher = Publisher.Publisher_ID

ORDER BY 
game.Franchise_ID Asc,
Release_Year asc;
""" # SQL Code to print out all the info in database
        cursor.execute(SQL_Code_Print_All) # Excute the SQL Code
        print(f"{UnderScore*127}") #UI
        print(f"|Title{space*36}|Main Character{space*6}|Genre{space*13}|REL{space*3}|Publisher{space*11}|Franchise{space*8}|") #Header UI
        print(f"|{UnderScore*41}|{UnderScore*20}|{UnderScore*18}|{UnderScore*6}|{UnderScore*20}|{UnderScore*17}|") #UI
        for game in cursor.fetchall(): # Print out all the info in database
            print(f"|{game[0]:<40} | {game[1]:<18} | {game[2]:<16} | {game[3]:<4} | {game[4]:<18} | {game[5]:<15} |")
            print(f"|{UnderScore*41}|{UnderScore*20}|{UnderScore*18}|{UnderScore*6}|{UnderScore*20}|{UnderScore*17}|") #UI
            #End
        #End
    #End

def Print_All_Selected_Franchise(): # Command 2
     print("") #Clean UI
     print("Select Franchise Option")
     with sqlite3.connect(DATABASE) as db: # Connect to Database
          cursor = db.cursor() # Create Cursor
          SQL_Code_Franchise = """
Select Franchise_ID, Franchise
From Franchise
""" # First SQL Code to print out Franchise to select
          cursor.execute(SQL_Code_Franchise) # Print out a list of Franchise to select
          print(f"{UnderScore*54}") #UI
          for franchise in cursor.fetchall(): # Print out Franchise to select
           print(f"|{franchise[0]:<2}| = |{franchise[1]:<46}|")
           print(f"|{UnderScore*2}|{UnderScore*3}|{UnderScore*46}|") #UI
          print("Return = Return back to Menu")
          while True: # While True Loop to ask for Franchise
              try: # Try Except to catch error or invalid input
                  Selected_Franchise = input("Select Franchise: ") #Ask for Franchise
                  if Selected_Franchise.lower() == 'return': # Return to Menu if input is return
                      Menu(Username)
                  SQL_Code_Print_Info = f"""
select game.Title, Main_Character.Main_Character_Name, Genre.Genre, Game.Release_Year, Franchise.Publisher, Franchise.Franchise, Franchise.Original_Creator
from game

JOIN Genre_Bridge on Genre_Bridge.Game_ID = Game.Game_ID
JOIN Genre on Genre.Genre_ID = Genre_Bridge.Genre_ID

JOIN Main_Character_Bridge on Main_character_bridge.Game_ID = game.Game_ID
JOIN Main_Character on Main_character.Main_Character_ID = Main_character_bridge.Main_Character_ID

Join Franchise on Game.Franchise_ID = Franchise.Franchise_ID

Where Game.Franchise_ID = {Selected_Franchise}

order by 
game.Franchise_ID Asc,
Release_Year asc
""" # SQL Code to print out all the info of selected Franchise based on user input
                  cursor.execute(SQL_Code_Print_Info) # Excute the SQL Code
                  print(f"{UnderScore*127}") #UI
                  print(f"|Title{space*36}|Main Character{space*6}|Genre{space*13}|REL{space*3}|Publisher{space*11}|Franchise{space*8}|") #Header UI
                  print(f"|{UnderScore*41}|{UnderScore*20}|{UnderScore*18}|{UnderScore*6}|{UnderScore*20}|{UnderScore*17}|") #UI
                  for game in cursor.fetchall(): #      Print out all the info of selected Franchise based on user input
                   print(f"|{game[0]:<40} | {game[1]:<18} | {game[2]:<16} | {game[3]:<4} | {game[4]:<18} | {game[5]:<15} |")
                   print(f"|{UnderScore*41}|{UnderScore*20}|{UnderScore*18}|{UnderScore*6}|{UnderScore*20}|{UnderScore*17}|") #UI
                  print("Select New Franchise? / 1")
                  Question = input("Return To Menu / 2?\n") # Ask to select new Franchise or Return to Menu
                  if Question == "1":
                      Print_All_Selected_Franchise()
                  elif Question == "2":
                      Menu(Username)
                  
              except: # If input is invalid or error, print Error
                  print("Error")
              #End

def Print_Game_Info(): # Command 3
    print("") #Clean UI
    print("Select Game Option")
    with sqlite3.connect(DATABASE) as db: # Connect to Database
          cursor = db.cursor() # Create Cursor
          SQL_Code_Game_List = """
Select Game_ID, Title
From Game
""" # First SQL Code to print out Game to select
          cursor.execute(SQL_Code_Game_List) # Print out a list of Game to select
          print(f"{UnderScore*54}") #UI
          for game in cursor.fetchall(): # Print out Game to select
           print(f"|{game[0]:<2}| = |{game[1]:<46}|")
           print(f"|{UnderScore*2}|{UnderScore*3}|{UnderScore*46}|") #UI
          print("Return = Return back to Menu")
          while True: # While True Loop to ask for Game
              try: #    Try Except to catch error or invalid input
                  Selected_Game = input("Select Game: ") #Ask for Game
                  if Selected_Game.lower() == 'return': # Return to Menu if input is return
                      Menu(Username)
                  SQL_Code_Game_Info = f"""
select game.Title, Main_Character.Main_Character_Name, Genre.Genre, Game.Release_Year, Franchise.Publisher, Franchise.Franchise, Franchise.Original_Creator
from game

JOIN Genre_Bridge on Genre_Bridge.Game_ID = Game.Game_ID
JOIN Genre on Genre.Genre_ID = Genre_Bridge.Genre_ID

JOIN Main_Character_Bridge on Main_character_bridge.Game_ID = game.Game_ID
JOIN Main_Character on Main_character.Main_Character_ID = Main_character_bridge.Main_Character_ID

Join Franchise on Game.Franchise_ID = Franchise.Franchise_ID

Where Game.Game_ID = {Selected_Game}

order by 
game.Franchise_ID Asc,
Release_Year asc
""" # SQL Code to print out all the info of selected Game based on user input
                  cursor.execute(SQL_Code_Game_Info) # Excute the SQL Code
                  print(f"{UnderScore*127}") #UI
                  print(f"|Title{space*36}|Main Character{space*6}|Genre{space*13}|REL{space*3}|Publisher{space*11}|Franchise{space*8}|") #Header UI
                  print(f"|{UnderScore*41}|{UnderScore*20}|{UnderScore*18}|{UnderScore*6}|{UnderScore*20}|{UnderScore*17}|") #UI
                  for Games in cursor.fetchall(): # Print out all the info of selected Game based on user input
                   print(f"|{Games[0]:<40} | {Games[1]:<18} | {Games[2]:<16} | {Games[3]:<4} | {Games[4]:<18} | {Games[5]:<15} |")
                   print(f"|{UnderScore*41}|{UnderScore*20}|{UnderScore*18}|{UnderScore*6}|{UnderScore*20}|{UnderScore*17}|") #UI
                  print("Select New Game? / 1")
                  Question = input("Return To Menu / 2?\n") #   Ask to select new Game or Return to Menu
                  if Question == "1":
                      Print_Game_Info()
                  elif Question == "2":
                      Menu(Username)
                  
              except: # If input is invalid or error,
                  print("Error")
              #End

def Print_MC_appeared_In(): # Command 4
    print("") #Clean UI
    print("Select Main_Character Option")
    with sqlite3.connect(DATABASE) as db: # Connect to Database
          cursor = db.cursor() # Create Cursor
          SQL_Code_MC = """
Select Main_Character_ID, Main_Character_Name
From Main_Character
""" # First SQL Code to print out Main_Character to select
          cursor.execute(SQL_Code_MC) # Print out a list of MC to select
          print(f"{UnderScore*54}") #UI
          for MC in cursor.fetchall(): # Print out MC to select
           print(f"|{MC[0]:<2}| = |{MC[1]:<46}|")
           print(f"|{UnderScore*2}|{UnderScore*3}|{UnderScore*46}|") #UI
          print("Return = Return back to Menu")
          while True: # While True Loop to ask for MC
              try: # Try Except to catch error or invalid input
                  Selected_MC = input("Select Main_Character: ") #Ask for MC
                  if Selected_MC.lower() == 'return': # Return to Menu if input is return
                      Menu(Username)
                  SQL_Code_Filter_MC = f"""
select game.Title, Main_Character.Main_Character_Name, Genre.Genre, Game.Release_Year, Franchise.Publisher, Franchise.Franchise, Franchise.Original_Creator
from game

JOIN Genre_Bridge on Genre_Bridge.Game_ID = Game.Game_ID
JOIN Genre on Genre.Genre_ID = Genre_Bridge.Genre_ID

JOIN Main_Character_Bridge on Main_character_bridge.Game_ID = game.Game_ID
JOIN Main_Character on Main_character.Main_Character_ID = Main_character_bridge.Main_Character_ID

Join Franchise on Game.Franchise_ID = Franchise.Franchise_ID

Where Main_Character_Bridge.Main_Character_ID = {Selected_MC}

order by 
game.Franchise_ID Asc,
Release_Year asc
""" # SQL Code to filter game by Main_Character based on user input
                  cursor.execute(SQL_Code_Filter_MC) # Execute the filtered SQL query
                  print(f"{UnderScore*127}") #UI
                  print(f"|Title{space*36}|Main Character{space*6}|Genre{space*13}|REL{space*3}|Publisher{space*11}|Franchise{space*8}|") #Header UI
                  print(f"|{UnderScore*41}|{UnderScore*20}|{UnderScore*18}|{UnderScore*6}|{UnderScore*20}|{UnderScore*17}|") #UI
                  for Game in cursor.fetchall(): # Print out all the game that filter by Main_Character based on user input
                   print(f"|{Game[0]:<40} | {Game[1]:<18} | {Game[2]:<16} | {Game[3]:<4} | {Game[4]:<18} | {Game[5]:<15} |")
                   print(f"|{UnderScore*41}|{UnderScore*20}|{UnderScore*18}|{UnderScore*6}|{UnderScore*20}|{UnderScore*17}|") #UI
                  print("Select New Main_Character? / 1")
                  Question = input("Return To Menu / 2?\n") # Ask to select new Main_Character or Return to Menu
                  if Question == "1":
                     Print_MC_appeared_In()
                  elif Question == "2":
                      Menu(Username)
                  
              except: # If input is invalid or error, print Error
                  print("Error")
              #End

def Print_Genre_filter(): # Command 5
    print("") #Clean UI
    print("Select Genre Option") 
    with sqlite3.connect(DATABASE) as db: # Connect to Database
          cursor = db.cursor() # Create Cursor
          SQL_Code_AllGenre = """
Select Genre_ID, Genre
From Genre
""" # First SQL Code to print out Genre to select
          cursor.execute(SQL_Code_AllGenre) # Print out a list of Genre to select
          print(f"{UnderScore*54}") #UI
          for Genre in cursor.fetchall(): # Print out Genre to select
           print(f"|{Genre[0]:<10}| = |{Genre[1]:<46}|")
           print(f"|{UnderScore*10}|{UnderScore*3}|{UnderScore*46}|") #UI
          print("Return = Return back to Menu") #UI for how to select Genre
          print("Finish = Finish selection") #UI for how to select Genre
          print("3 Selection max") #UI for how to select Genre
          Genre1 = 0 # Variable to store Genre1 selection, default is 0 which is not a valid Genre_ID in database, so if user only select 1 Genre, it will only filter by Genre1 and ignore Genre2 and Genre3 since they are 0
          Genre2 = 0
          Genre3 = 0
          def filter_Genre(Genre1, Genre2, Genre3, cursor): # Sub-Function for Command 5
                    SQL_Code_Filter_Genre  = f"""
                          select game.Title, Main_Character.Main_Character_Name, Genre.Genre, Game.Release_Year, Franchise.Publisher, Franchise.Franchise, Franchise.Original_Creator
                          from game
                          
                          JOIN Genre_Bridge on Genre_Bridge.Game_ID = Game.Game_ID
                          JOIN Genre on Genre.Genre_ID = Genre_Bridge.Genre_ID

                          JOIN Main_Character_Bridge on Main_character_bridge.Game_ID = game.Game_ID
                          JOIN Main_Character on Main_character.Main_Character_ID = Main_character_bridge.Main_Character_ID

                          Join Franchise on Game.Franchise_ID = Franchise.Franchise_ID

                          Where (Genre_Bridge.Genre_ID = {Genre1} or Genre_Bridge.Genre_ID = {Genre2} or Genre_Bridge.Genre_ID = {Genre3})

                          ORDER BY
                          game.Franchise_ID Asc,
                          Release_Year asc
                          """ # SQL Code to filter game by Genre based on user input
                    cursor.execute(SQL_Code_Filter_Genre) # Excute the SQL Code
                    print(f"{UnderScore*127}") #UI
                    print(f"|Title{space*36}|Main Character{space*6}|Genre{space*13}|REL{space*3}|Publisher{space*11}|Franchise{space*8}|") #Header UI
                    print(f"|{UnderScore*41}|{UnderScore*20}|{UnderScore*18}|{UnderScore*6}|{UnderScore*20}|{UnderScore*17}|") #UI
                    for Game in cursor.fetchall(): # Print out all the game that filter by Genre based on user input
                        print(f"|{Game[0]:<40} | {Game[1]:<18} | {Game[2]:<16} | {Game[3]:<4} | {Game[4]:<18} | {Game[5]:<15} |")
                        print(f"|{UnderScore*41}|{UnderScore*20}|{UnderScore*18}|{UnderScore*6}|{UnderScore*20}|{UnderScore*17}|") #UI
                    print("Select New Genre? / 1")
                    Question = input("Return To Menu / 2?\n") # Ask to select new Genre or Return to Menu
                    if Question == "1":
                        Print_Genre_filter()
                    elif Question == "2":
                        Menu(Username)
          while True: # While True Loop to ask for Genre
                  try: # Try Except to catch error or invalid input
                      Selected_Genre = input("Select Genre: ") #Ask for Genre
                      if Selected_Genre.lower() == 'return': # Return to Menu if input is return
                          Menu(Username) # If user select return, it will return to Menu
                      elif Selected_Genre.lower() == "finish": # If user select finish, it will filter by Genre1 which is 0, since there is no Genre with Genre_ID 0 in database, it will return empty result, and then it will ask for Genre again until user select a valid Genre or select return to Menu
                          filter_Genre(Genre1, Genre2, Genre3, cursor)
                      Genre1 = Selected_Genre # Store the selected Genre in Genre1 variable
                      Selected_Genre2 = input("Select another Genre?: ") #Ask for Genre
                      if Selected_Genre2.lower() == 'return': 
                          Menu(Username) 
                      elif Selected_Genre2.lower() == "finish":
                          filter_Genre(Genre1, Genre2, Genre3, cursor)
                          Genre2 = Selected_Genre2
                          Selected_Genre3 = input("Select Last Genre?: ") #Ask for Genre
                      if Selected_Genre3.lower() == 'return':
                          Menu(Username)
                      elif Selected_Genre3.lower() == "finish":
                          filter_Genre(Genre1, Genre2, Genre3, cursor)
                          Genre3 = Selected_Genre3
                          filter_Genre(Genre1, Genre2, Genre3, cursor)
                  except: # If input is invalid or error, print Error
                      print("Error")
                              
              
                #End

def print_REL_filter(): # Command 6
    print("") #Clean UI
    print("Input Date")
    with sqlite3.connect(DATABASE) as db: # Connect to Database
          cursor = db.cursor() # Create Cursor
          print("Command") #UI for how to input date
          print("> = Higher") #UI for how to input date
          print("< = Lower") #UI for how to input date
          print("Example: > 2020") #UI for how to input date
          print("Example2: < 2019") #UI for how to input date
          print("Return = Return back to Menu") #UI for how to input date
          while True: # While True Loop to ask for Date
              try: # Try Except to catch error or invalid input
                  Selected_Date = input("Command: ") #Ask for Date
                  if Selected_Date.lower() == 'return': # Return to Menu if input is return
                      Menu(Username)
                  SQL_Code_Filter_Date = f"""
select game.Title, Main_Character.Main_Character_Name, Genre.Genre, Game.Release_Year, Franchise.Publisher, Franchise.Franchise, Franchise.Original_Creator
from game

JOIN Genre_Bridge on Genre_Bridge.Game_ID = Game.Game_ID
JOIN Genre on Genre.Genre_ID = Genre_Bridge.Genre_ID

JOIN Main_Character_Bridge on Main_character_bridge.Game_ID = game.Game_ID
JOIN Main_Character on Main_character.Main_Character_ID = Main_character_bridge.Main_Character_ID

Join Franchise on Game.Franchise_ID = Franchise.Franchise_ID

Where Game.Release_Year {Selected_Date}

order by 
game.Franchise_ID Asc,
Release_Year asc
""" # SQL Code to filter game by Release Year based on user input
                  cursor.execute(SQL_Code_Filter_Date) # Excute the SQL Code
                  print(f"{UnderScore*127}") #UI
                  print(f"|Title{space*36}|Main Character{space*6}|Genre{space*13}|REL{space*3}|Publisher{space*11}|Franchise{space*8}|") #Header UI
                  print(f"|{UnderScore*41}|{UnderScore*20}|{UnderScore*18}|{UnderScore*6}|{UnderScore*20}|{UnderScore*17}|") #UI
                  for Game in cursor.fetchall(): # Print out all the game that filter by Release Year based on user input
                   print(f"|{Game[0]:<40} | {Game[1]:<18} | {Game[2]:<16} | {Game[3]:<4} | {Game[4]:<18} | {Game[5]:<15} |")
                   print(f"|{UnderScore*41}|{UnderScore*20}|{UnderScore*18}|{UnderScore*6}|{UnderScore*20}|{UnderScore*17}|") #UI
                  print("Select New Date? / 1")
                  Question = input("Return To Menu / 2?\n") # Ask to select new Date or Return to Menu
                  if Question == "1":
                     Print_MC_appeared_In()
                  elif Question == "2":
                      Menu(Username)
                  
              except: # If input is invalid or error, print Error
                  print("Error")
              #End

def Print_All_Selected_Publisher(): #Command 7
    print("")
    print("Select Publisher Option")
    with sqlite3.connect(DATABASE) as db: # Connect to Database
          cursor = db.cursor() # Create Cursor
          SQL_Code_Print_Publisher = """ 
Select Publisher.Publisher_ID, Publisher.Publisher
From Publisher
""" #First SQL Code to print out Publisher
          cursor.execute(SQL_Code_Print_Publisher) # Excute the first SQL Code
          print(f"{UnderScore*54}") #UI
          for Publisher in cursor.fetchall(): # Print out the Publisher to select
           print(f"|{Publisher[0]:<2}| = |{Publisher[1]:<46}|") 
           print(f"|{UnderScore*2}|{UnderScore*3}|{UnderScore*46}|") #UI
          print("Return = Return back to Menu")
          while True: # While True Loop to ask for Publisher
              try: # Try Except to catch error or invalid input
                  Selected_Publisher = input("Select Publisher: ") #Ask for Publisher
                  if Selected_Publisher.lower() == 'return': # Return to Menu if input is return
                      Menu(Username)
                  Print_Selected = f"""
SELECT 
Game.Title,
Main_Character.Main_Character_Name,
Genre.Genre,
Game.Release_Year,
Publisher.Publisher,
Franchise.Franchise,
Franchise.Original_Creator

FROM Game

JOIN Genre_Bridge on Genre_Bridge.Game_ID = Game.Game_ID
JOIN Genre on Genre.Genre_ID = Genre_Bridge.Genre_ID

JOIN Main_Character_Bridge on Main_character_bridge.Game_ID = game.Game_ID
JOIN Main_Character on Main_character.Main_Character_ID = Main_character_bridge.Main_Character_ID

Join Franchise on Game.Franchise_ID = Franchise.Franchise_ID
Join Publisher on Franchise.Publisher = Publisher.Publisher_ID

Where Publisher.Publisher_ID = {Selected_Publisher}

ORDER BY 
game.Franchise_ID Asc,
Release_Year asc;
""" # Second SQL Code to print out all game by selected Publisher
                  cursor.execute(Print_Selected) # Excute the second SQL Code
                  print(f"{UnderScore*127}") #UI
                  print(f"|Title{space*36}|Main Character{space*6}|Genre{space*13}|REL{space*3}|Publisher{space*11}|Franchise{space*8}|") #Header UI
                  print(f"|{UnderScore*41}|{UnderScore*20}|{UnderScore*18}|{UnderScore*6}|{UnderScore*20}|{UnderScore*17}|") #UI
                  for Game in cursor.fetchall(): # Print out all the game by selected Publisher
                   print(f"|{Game[0]:<40} | {Game[1]:<18} | {Game[2]:<16} | {Game[3]:<4} | {Game[4]:<18} | {Game[5]:<15} |")
                   print(f"|{UnderScore*41}|{UnderScore*20}|{UnderScore*18}|{UnderScore*6}|{UnderScore*20}|{UnderScore*17}|") #UI
                  print("Select New Publisher? / 1")
                  Question = input("Return To Menu / 2?\n") # Ask to select new Publisher or Return to Menu
                  if Question == "1":
                     Print_All_Selected_Publisher()
                  elif Question == "2":
                      Menu(Username)
                  
              except: # If input is invalid or error, print Error
                  print("Error")
              #End
                    
                


def Menu(Username):
    print("")
    print("Type Command / h = Help\n")
    print("1 = Print All (Every Info in Database)")
    print("2 = Print All The Games Info From Selected Franchise")
    print("3 = Print The Selected The Game Info From Database")
    print("4 = Print All The Game That Selected Main Character Appeared In")
    print("5 = Print All Game By Filter Genre")
    print("6 = Print Game By Specific Release date")
    print("7 = Print all game by Selected Publisher")
    print("exit = exit")
    while True:
            try:
                command = input(f'C:/User/{Username}>')
                if command.lower() == "help":
                    print("Help yourself")
                    Menu(Username)
                elif command.lower() == "exit":
                    break
                elif int(command) == 1:
                    Print_All()
                    Return_Menu()
                elif int(command) == 2:
                    Print_All_Selected_Franchise()
                elif int(command) == 3:
                    Print_Game_Info()
                elif int(command) == 4:
                    Print_MC_appeared_In()
                elif int(command) == 5:
                    Print_Genre_filter()
                elif int(command) == 6:
                    print_REL_filter()
                elif int(command) == 7:
                    Print_All_Selected_Publisher()
                else:
                    raise
            except:
                print("Unknown Command / Error")
                

                
if __name__ == "__main__":
    Skip_Loading = True
    Skip_Security_Check = True
    Load()
    Username = Security()
    Menu(Username)
