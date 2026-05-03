import sqlite3
import random
import time
import itertools
import threading
import sys
DATABASE = 'Game_Franchise.db'
space = " "
UnderScore = "_"
No_line = False

def Load(): # Load Animation
    done = False
    if Skip_Loading == True:
        done = True
    else:
        def animation():
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

def Boot(): #Unfinish indefinitely
    done = False
    while done == False:
        sys.stdout.write(f"\r{random.randbytes(1)}")
        sys.stdout.flush()
        time.sleep(0.1)

def Security(): # Security Check
    Username = "Unknown"
    Password = "idk"
    if Skip_Security_Check == True:
        return Username
    else:
        print("Input your Username")
        Input_Username = input("Username: ")
        Username = Input_Username
        print("Password hint: Acronym for I don't Know")
        while True:
            try:
                 Input_Password = input("Password: ")
                 if Input_Password.lower() != Password:
                     raise
                 else:
                     return Username
            except:
                print('Invalid Input / Incorrect Password')
   
def Return_Menu(): # Quick Return To Menu Function
        while True:
            try:
                 Question = input("Return To Menu? / Y?\n")
                 if Question.lower() != "y":
                     raise
                 elif Question.lower() == "y":
                     Menu(Username)
            except:
                print("Error")

def Print_All(): #Command 1
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = """
SELECT 
Game.Title,
Main_Character.Main_Character_Name,
Genre.Genre, Game.Release_Year,
Franchise.Publisher,
Franchise.Franchise,
Franchise.Original_Creator

FROM Game

JOIN Genre_Bridge on Genre_Bridge.Game_ID = Game.Game_ID
JOIN Genre on Genre.Genre_ID = Genre_Bridge.Genre_ID

JOIN Main_Character_Bridge on Main_character_bridge.Game_ID = game.Game_ID
JOIN Main_Character on Main_character.Main_Character_ID = Main_character_bridge.Main_Character_ID

Join Franchise on Game.Franchise_ID = Franchise.Franchise_ID

ORDER BY 
game.Franchise_ID Asc,
Release_Year asc;
"""
        cursor.execute(sql)
        result = cursor.fetchall()
        print(f"{UnderScore*127}")
        print(f"|Title{space*36}|Main Character{space*6}|Genre{space*13}|REL{space*3}|Publisher{space*11}|Franchise{space*8}|")
        print(f"|{UnderScore*41}|{UnderScore*20}|{UnderScore*18}|{UnderScore*6}|{UnderScore*20}|{UnderScore*17}|")
        for game in result:
            print(f"|{game[0]:<40} | {game[1]:<18} | {game[2]:<16} | {game[3]:<4} | {game[4]:<18} | {game[5]:<15} |")
            print(f"|{UnderScore*41}|{UnderScore*20}|{UnderScore*18}|{UnderScore*6}|{UnderScore*20}|{UnderScore*17}|")
            #End

def Print_All_Selected_Franchise(): # Command 2
     print("")
     print("Select Franchise Option")
     with sqlite3.connect(DATABASE) as db:
          cursor = db.cursor()
          sql1 = """
Select Franchise_ID, Franchise
From Franchise
"""
          cursor.execute(sql1) # Print out a list of Franchise to select
          print(f"{UnderScore*54}")
          for franchise in cursor.fetchall():
           print(f"|{franchise[0]:<2}| = |{franchise[1]:<46}|")
           print(f"|{UnderScore*2}|{UnderScore*3}|{UnderScore*46}|")
          print("Return = Return back to Menu")
          while True:
              try:
                  Selected_Franchise = input("Select Franchise: ") #Ask for Franchise
                  if Selected_Franchise.lower() == 'return':
                      Menu(Username)
                  sql2 = f"""
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
"""
                  cursor.execute(sql2)
                  print(f"{UnderScore*127}")
                  print(f"|Title{space*36}|Main Character{space*6}|Genre{space*13}|REL{space*3}|Publisher{space*11}|Franchise{space*8}|")
                  print(f"|{UnderScore*41}|{UnderScore*20}|{UnderScore*18}|{UnderScore*6}|{UnderScore*20}|{UnderScore*17}|")
                  for game in cursor.fetchall():
                   print(f"|{game[0]:<40} | {game[1]:<18} | {game[2]:<16} | {game[3]:<4} | {game[4]:<18} | {game[5]:<15} |")
                   print(f"|{UnderScore*41}|{UnderScore*20}|{UnderScore*18}|{UnderScore*6}|{UnderScore*20}|{UnderScore*17}|")
                  print("Select New Franchise? / 1")
                  Question = input("Return To Menu / 2?\n")
                  if Question == "1":
                      Print_All_Selected_Franchise()
                  elif Question == "2":
                      Menu(Username)
                  
              except:
                  print("Error")
              #End

def Print_Game_Info(): # Command 3
    print("")
    print("Select Game Option")
    with sqlite3.connect(DATABASE) as db:
          cursor = db.cursor()
          sql1 = """
Select Game_ID, Title
From Game
"""
          cursor.execute(sql1) # Print out a list of Game to select
          print(f"{UnderScore*54}")
          for game in cursor.fetchall():
           print(f"|{game[0]:<2}| = |{game[1]:<46}|")
           print(f"|{UnderScore*2}|{UnderScore*3}|{UnderScore*46}|")
          print("Return = Return back to Menu")
          while True:
              try:
                  Selected_Game = input("Select Game: ") #Ask for Game
                  if Selected_Game.lower() == 'return':
                      Menu(Username)
                  sql2 = f"""
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
"""
                  cursor.execute(sql2)
                  print(f"{UnderScore*127}")
                  print(f"|Title{space*36}|Main Character{space*6}|Genre{space*13}|REL{space*3}|Publisher{space*11}|Franchise{space*8}|")
                  print(f"|{UnderScore*41}|{UnderScore*20}|{UnderScore*18}|{UnderScore*6}|{UnderScore*20}|{UnderScore*17}|")
                  for Games in cursor.fetchall():
                   print(f"|{Games[0]:<40} | {Games[1]:<18} | {Games[2]:<16} | {Games[3]:<4} | {Games[4]:<18} | {Games[5]:<15} |")
                   print(f"|{UnderScore*41}|{UnderScore*20}|{UnderScore*18}|{UnderScore*6}|{UnderScore*20}|{UnderScore*17}|")
                  print("Select New Game? / 1")
                  Question = input("Return To Menu / 2?\n")
                  if Question == "1":
                      Print_Game_Info()
                  elif Question == "2":
                      Menu(Username)
                  
              except:
                  print("Error")
              #End

def Print_MC_appeared_In(): # Command 4
    print("")
    print("Select Main_Character Option")
    with sqlite3.connect(DATABASE) as db:
          cursor = db.cursor()
          sql1 = """
Select Main_Character_ID, Main_Character_Name
From Main_Character
"""
          cursor.execute(sql1) # Print out a list of MC to select
          print(f"{UnderScore*54}")
          for MC in cursor.fetchall():
           print(f"|{MC[0]:<2}| = |{MC[1]:<46}|")
           print(f"|{UnderScore*2}|{UnderScore*3}|{UnderScore*46}|")
          print("Return = Return back to Menu")
          while True:
              try:
                  Selected_MC = input("Select Main_Character: ") #Ask for MC
                  if Selected_MC.lower() == 'return':
                      Menu(Username)
                  sql2 = f"""
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
"""
                  cursor.execute(sql2)
                  print(f"{UnderScore*127}")
                  print(f"|Title{space*36}|Main Character{space*6}|Genre{space*13}|REL{space*3}|Publisher{space*11}|Franchise{space*8}|")
                  print(f"|{UnderScore*41}|{UnderScore*20}|{UnderScore*18}|{UnderScore*6}|{UnderScore*20}|{UnderScore*17}|")
                  for Game in cursor.fetchall():
                   print(f"|{Game[0]:<40} | {Game[1]:<18} | {Game[2]:<16} | {Game[3]:<4} | {Game[4]:<18} | {Game[5]:<15} |")
                   print(f"|{UnderScore*41}|{UnderScore*20}|{UnderScore*18}|{UnderScore*6}|{UnderScore*20}|{UnderScore*17}|")
                  print("Select New Main_Character? / 1")
                  Question = input("Return To Menu / 2?\n")
                  if Question == "1":
                     Print_MC_appeared_In()
                  elif Question == "2":
                      Menu(Username)
                  
              except:
                  print("Error")
              #End

def Print_Genre_filter(): # Command 5
    print("")
    print("Select Genre Option")
    with sqlite3.connect(DATABASE) as db:
          cursor = db.cursor()
          sql1 = """
Select Genre_ID, Genre
From Genre
"""
          cursor.execute(sql1) # Print out a list of Genre to select
          print(f"{UnderScore*54}")
          for Genre in cursor.fetchall():
           print(f"|{Genre[0]:<10}| = |{Genre[1]:<46}|")
           print(f"|{UnderScore*10}|{UnderScore*3}|{UnderScore*46}|")
          print("Return = Return back to Menu")
          print("Finish = Finish selection")
          print("3 Selection max")
          Genre1 = 0
          Genre2 = 0
          Genre3 = 0
          while True:
              try:
                  Selected_Genre = input("Select Genre: ") #Ask for Genre
                  if Selected_Genre.lower() == 'return':
                      Menu(Username)
                  elif Selected_Genre.lower() == "finish":
                      filter_Genre(Genre1, Genre2, Genre3)
                  Genre1 = Selected_Genre
                  Selected_Genre2 = input("Select another Genre?: ") #Ask for Genre
                  if Selected_Genre2.lower() == 'return':
                    Menu(Username)
                  elif Selected_Genre2.lower() == "finish":
                      filter_Genre(Genre1, Genre2, Genre3)
                  Genre2 = Selected_Genre2
                  Selected_Genre3 = input("Select Last Genre?: ") #Ask for Genre
                  if Selected_Genre3.lower() == 'return':
                    Menu(Username)
                  elif Selected_Genre3.lower() == "finish":
                    filter_Genre(Genre1, Genre2, Genre3)
                  Genre3 = Selected_Genre3
                  filter_Genre(Genre1, Genre2, Genre3)

              except:
                print("Error")
                #End

def filter_Genre(Genre1, Genre2, Genre3): # Sub-Function for Command 5
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql2  = f"""
select game.Title, Main_Character.Main_Character_Name, Genre.Genre, Game.Release_Year, Franchise.Publisher, Franchise.Franchise, Franchise.Original_Creator
from game

JOIN Genre_Bridge on Genre_Bridge.Game_ID = Game.Game_ID
JOIN Genre on Genre.Genre_ID = Genre_Bridge.Genre_ID

JOIN Main_Character_Bridge on Main_character_bridge.Game_ID = game.Game_ID
JOIN Main_Character on Main_character.Main_Character_ID = Main_character_bridge.Main_Character_ID

Join Franchise on Game.Franchise_ID = Franchise.Franchise_ID

Where (Genre_Bridge.Genre_ID = {Genre1} or Genre_Bridge.Genre_ID = {Genre2} or Genre_Bridge.Genre_ID = {Genre3})

order by 
game.Franchise_ID Asc,
Release_Year asc
"""
        cursor.execute(sql2)
        print(f"{UnderScore*127}")
        print(f"|Title{space*36}|Main Character{space*6}|Genre{space*13}|REL{space*3}|Publisher{space*11}|Franchise{space*8}|")
        print(f"|{UnderScore*41}|{UnderScore*20}|{UnderScore*18}|{UnderScore*6}|{UnderScore*20}|{UnderScore*17}|")
        for Game in cursor.fetchall():
            print(f"|{Game[0]:<40} | {Game[1]:<18} | {Game[2]:<16} | {Game[3]:<4} | {Game[4]:<18} | {Game[5]:<15} |")
            print(f"|{UnderScore*41}|{UnderScore*20}|{UnderScore*18}|{UnderScore*6}|{UnderScore*20}|{UnderScore*17}|")
        print("Select New Genre? / 1")
        Question = input("Return To Menu / 2?\n")
        if Question == "1":
            Print_Genre_filter()
        elif Question == "2":
            Menu(Username)

def print_REL_filter(): # Command 6
    print("")
    print("Input Date")
    with sqlite3.connect(DATABASE) as db:
          cursor = db.cursor()
          print("Command")
          print("> = Higher")
          print("< = Lower")
          print("Example: > 2020")
          print("Example2: < 2019")
          print("Return = Return back to Menu")
          while True:
              try:
                  Selected_Date = input("Command: ") #Ask for Date
                  if Selected_Date.lower() == 'return':
                      Menu(Username)
                  sql1 = f"""
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
"""
                  cursor.execute(sql1)
                  print(f"{UnderScore*127}")
                  print(f"|Title{space*36}|Main Character{space*6}|Genre{space*13}|REL{space*3}|Publisher{space*11}|Franchise{space*8}|")
                  print(f"|{UnderScore*41}|{UnderScore*20}|{UnderScore*18}|{UnderScore*6}|{UnderScore*20}|{UnderScore*17}|")
                  for Game in cursor.fetchall():
                   print(f"|{Game[0]:<40} | {Game[1]:<18} | {Game[2]:<16} | {Game[3]:<4} | {Game[4]:<18} | {Game[5]:<15} |")
                   print(f"|{UnderScore*41}|{UnderScore*20}|{UnderScore*18}|{UnderScore*6}|{UnderScore*20}|{UnderScore*17}|")
                  print("Select New Date? / 1")
                  Question = input("Return To Menu / 2?\n")
                  if Question == "1":
                     Print_MC_appeared_In()
                  elif Question == "2":
                      Menu(Username)
                  
              except:
                  print("Error")
              #End

def Print_All_Selected_Publisher(): #Unfinish
    print("")
    print("Select Publisher Option")
    with sqlite3.connect(DATABASE) as db:
          cursor = db.cursor()
          sql1 = """
Select Publisher
From Franchise
"""
          cursor.execute(sql1) # Print out a list of MC to select
          print(f"{UnderScore*54}")
          for MC in cursor.fetchall():
           print(f"{MC[0]}")
           print(f"|{UnderScore*2}|{UnderScore*3}|{UnderScore*46}|")
          print("Return = Return back to Menu")
          while True:
              try:
                  Selected_MC = input("Select Main_Character: ") #Ask for MC
                  if Selected_MC.lower() == 'return':
                      Menu(Username)
                  sql2 = f"""
select game.Title, Main_Character.Main_Character_Name, Genre.Genre, Game.Release_Year, Franchise.Publisher, Franchise.Franchise, Franchise.Original_Creator
from game

JOIN Genre_Bridge on Genre_Bridge.Game_ID = Game.Game_ID
JOIN Genre on Genre.Genre_ID = Genre_Bridge.Genre_ID

JOIN Main_Character_Bridge on Main_character_bridge.Game_ID = game.Game_ID
JOIN Main_Character on Main_character.Main_Character_ID = Main_character_bridge.Main_Character_ID

Join Franchise on Game.Franchise_ID = Franchise.Franchise_ID

Where Franchise.Publisher = {Selected_MC}

order by 
game.Franchise_ID Asc,
Release_Year asc
"""
                  cursor.execute(sql2)
                  print(f"{UnderScore*127}")
                  print(f"|Title{space*36}|Main Character{space*6}|Genre{space*13}|REL{space*3}|Publisher{space*11}|Franchise{space*8}|")
                  print(f"|{UnderScore*41}|{UnderScore*20}|{UnderScore*18}|{UnderScore*6}|{UnderScore*20}|{UnderScore*17}|")
                  for Game in cursor.fetchall():
                   print(f"|{Game[0]:<40} | {Game[1]:<18} | {Game[2]:<16} | {Game[3]:<4} | {Game[4]:<18} | {Game[5]:<15} |")
                   print(f"|{UnderScore*41}|{UnderScore*20}|{UnderScore*18}|{UnderScore*6}|{UnderScore*20}|{UnderScore*17}|")
                  print("Select New Main_Character? / 1")
                  Question = input("Return To Menu / 2?\n")
                  if Question == "1":
                     Print_MC_appeared_In()
                  elif Question == "2":
                      Menu(Username)
                  
              except:
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
                else:
                    raise
            except:
                print("Unknown Command / Error")
                

                
if __name__ == "__main__":
    Skip_Loading = False
    Skip_Security_Check = False
    Load()
    Username = Security()
    Menu(Username)
