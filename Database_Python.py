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
UnderScore = "_" # Variable for UI
UpperScore = "‾" # Variable for UI

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

def return_shortcut(Input_Code): # Function to check if user input return to return to Menu
    Trigger_Line = "return"
    if Input_Code.lower() == "return":
        Menu(Username)

def Retry_Return(Message_1, Message_2, fn, cursor): # Function to ask user if they want to retry the same function or return to menu
    Highest_Char = 0
    Msg1_char_count = len(Message_1)
    Msg2_char_count = len(Message_2)
    if Msg1_char_count > Msg2_char_count:
        Highest_Char = Msg1_char_count
    elif Msg2_char_count > Msg1_char_count:
        Highest_Char = Msg2_char_count
    print(f"""
{UnderScore*(Highest_Char + 10)}
| 1 | = |{Message_1:<{Highest_Char + 1}}|
| 2 | = |{Message_2:<{Highest_Char + 1}}|
{UpperScore*(Highest_Char + 10)}
          """)
    while True: # While True Loop to ask for Return to Menu
        try: # Try Except to catch error or invalid input
             Question = input(f"C:/User/{Username}>") # Ask for input
             if Question == "1": # If input is 1, execute the function
                 return fn(cursor)
             elif Question == "2": # If input is 2, return to Menu
                 Menu(Username)
             else:
                 raise # Raise error to ask for input again until user input 1 or 2
        except: # If input is invalid or error, print Error
            print("Error")

def print_option(option_data): # Function to print out the option to select in a table format
    highest_char_option = 0
    highest_char_ID = 0
    for option in option_data:
        if len(str(option[0])) > highest_char_ID:
            highest_char_ID = len(str(option[0]))
        if len(str(option[1])) > highest_char_option:
            highest_char_option = len(str(option[1]))

    gap_space = 1 # Add space to the highest character count for UI
    extra_space = 9 # Extra space for the header and UI
    symbol_space = 3 # Space for the symbols in UI
    length = highest_char_ID + highest_char_option + extra_space

    highest_char_ID = highest_char_ID + gap_space
    highest_char_option = highest_char_option + gap_space

    print(f"{UnderScore*(length)}") #UI
    for option in option_data:
        print(f"|{option[0]:<{highest_char_ID}}| = |{option[1]:<{highest_char_option}}|") # Print out the option to select
        print(f"|{UnderScore*highest_char_ID}|{UnderScore*symbol_space}|{UnderScore*highest_char_option}|") #UI

def print_data(data_result): # Function to print out the data in a table format
    highest_char_Title = 0
    highest_char_Main_Character = 0
    highest_char_Genre = 0
    highest_char_Release_Year = 0
    highest_char_Publisher = 0
    highest_char_Franchise = 0
   
    for data in data_result:
        # Calculate the highest character count for each column
        if len(str(data[0])) > highest_char_Title:
            highest_char_Title = len(str(data[0]))
        if len(str(data[1])) > highest_char_Main_Character:
            highest_char_Main_Character = len(str(data[1]))
        if len(str(data[2])) > highest_char_Genre:
            highest_char_Genre = len(str(data[2]))
        if len(str(data[3])) > highest_char_Release_Year:
            highest_char_Release_Year = len(str(data[3]))
        if len(str(data[4])) > highest_char_Publisher:
            highest_char_Publisher = len(str(data[4]))
        if len(str(data[5])) > highest_char_Franchise:
            highest_char_Franchise = len(str(data[5]))
    
    #title for each column
    Title = "Title"
    Main_Character = "Main Character"
    Genre = "Genre"
    Release_Year = "REL"
    Publisher = "Publisher"
    Franchise = "Franchise"

    gap_space = 1 # Add space to the highest character count for UI
    extra_space = 13 # Extra space for the header and UI

    if len(Title) > highest_char_Title:
        highest_char_Title = len(Title)
    if len(Main_Character) > highest_char_Main_Character:
        highest_char_Main_Character = len(Main_Character)
    if len(Genre) > highest_char_Genre:
        highest_char_Genre = len(Genre)
    if len(Release_Year) > highest_char_Release_Year:
        highest_char_Release_Year = len(Release_Year)
    if len(Publisher) > highest_char_Publisher:
        highest_char_Publisher = len(Publisher)
    if len(Franchise) > highest_char_Franchise:
        highest_char_Franchise = len(Franchise)

    length = highest_char_Title + highest_char_Main_Character + highest_char_Genre + highest_char_Release_Year + highest_char_Publisher + highest_char_Franchise + extra_space
    highest_char_Title = highest_char_Title + gap_space
    highest_char_Main_Character = highest_char_Main_Character + gap_space
    highest_char_Genre = highest_char_Genre + gap_space
    highest_char_Release_Year = highest_char_Release_Year + gap_space
    highest_char_Publisher = highest_char_Publisher + gap_space
    highest_char_Franchise = highest_char_Franchise + gap_space

    print(f"{UnderScore*(length)}") #UI
    print(f"|{Title:<{highest_char_Title}}|{Main_Character:<{highest_char_Main_Character}}|{Genre:<{highest_char_Genre}}|{Release_Year:<{highest_char_Release_Year}}|{Publisher:<{highest_char_Publisher}}|{Franchise:<{highest_char_Franchise}}|") #Header UI
    print(f"|{UnderScore*highest_char_Title}|{UnderScore*highest_char_Main_Character}|{UnderScore*highest_char_Genre}|{UnderScore*highest_char_Release_Year}|{UnderScore*highest_char_Publisher}|{UnderScore*highest_char_Franchise}|") #UI
    for Game in data_result: # Print out all the game by selected Publisher
        print(f"|{Game[0]:<{highest_char_Title}}|{Game[1]:<{highest_char_Main_Character}}|{Game[2]:<{highest_char_Genre}}|{Game[3]:<{highest_char_Release_Year}}|{Game[4]:<{highest_char_Publisher}}|{Game[5]:<{highest_char_Franchise}}|")
        print(f"|{UnderScore*highest_char_Title}|{UnderScore*highest_char_Main_Character}|{UnderScore*highest_char_Genre}|{UnderScore*highest_char_Release_Year}|{UnderScore*highest_char_Publisher}|{UnderScore*highest_char_Franchise}|") #UI

def SQL_Code_Options(ID, Name, Table): # Generic SQL Code for print out the option to select based on user input
    SQL_Code = f"""
Select {ID}, {Name}
From {Table}
    """
    return SQL_Code

def SQL_Code_Selected_Data(Where_Clause, Selected_Data): # Generic SQL Code for filter data based on user input
        SQL_Code = f"""
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

Where {Where_Clause} = {Selected_Data}

ORDER BY 
game.Franchise_ID Asc,
Release_Year asc;
""" # SQL Code to print out all game by selected Publisher
        return SQL_Code

def Print_All(cursor): #Command 1
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
"""
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

def Print_All_Selected_Franchise(cursor): # Command 2
     print("") #Clean UI
     print("Select Franchise Option")
     cursor.execute(SQL_Code_Options("Franchise_ID", "Franchise", "Franchise")) # Print out a list of Franchise to select
     print_option(cursor.fetchall()) # Call the print_option function to print out the Franchise to select
     print("Return = Return back to Menu")
     while True: # While True Loop to ask for Franchise
         try: # Try Except to catch error or invalid input
            Selected_Franchise = input("Select Franchise: ") #Ask for Franchise
            return_shortcut(Selected_Franchise) # If user input return, it will return to Menu
            cursor.execute(SQL_Code_Selected_Data("Franchise.Franchise_ID", Selected_Franchise)) # Excute the SQL Code
            print_data(cursor.fetchall()) # Call the print_data function to print out all the info of selected Franchise in a table format
            Retry_Return("Select New Franchise?", "Return To Menu?", Print_All_Selected_Franchise, cursor)
         except: # If input is invalid or error, print Error
            print("Error")
        #End

def Print_Game_Info(cursor): # Command 3
    print("") #Clean UI
    print("Select Game Option")
    cursor.execute(SQL_Code_Options("Game_ID", "Title", "Game")) # Print out a list of Game to select
    print_option(cursor.fetchall()) # Call the print_option function to print out the Game to select
    print("Return = Return back to Menu")
    while True: # While True Loop to ask for Game
        try: #    Try Except to catch error or invalid input
            Selected_Game = input("Select Game: ") #Ask for Game
            return_shortcut(Selected_Game) # If user input return, it will return to Menu
            cursor.execute(SQL_Code_Selected_Data("Game.Game_ID", Selected_Game)) # Excute the SQL Code
            print_data(cursor.fetchall()) # Call the print_data function to print out all the info of selected Game in a table format
            Retry_Return("Select New Game?", "Return To Menu?", Print_Game_Info, cursor)
        except: # If input is invalid or error,
            print("Error")
        #End

def Print_MC_appeared_In(cursor): # Command 4
    print("") #Clean UI
    print("Select Main_Character Option")
    cursor.execute(SQL_Code_Options("Main_Character_ID", "Main_Character_Name", "Main_Character")) # Print out a list of MC to select
    print_option(cursor.fetchall()) # Call the print_option function to print out the MC to select
    print("Return = Return back to Menu")
    while True: # While True Loop to ask for MC
        try: # Try Except to catch error or invalid input
            Selected_MC = input("Select Main_Character: ") #Ask for MC
            return_shortcut(Selected_MC) # If user input return, it will return to Menu
            cursor.execute(SQL_Code_Selected_Data("Main_Character_Bridge.Main_Character_ID", Selected_MC)) # Execute the filtered SQL query
            print_data(cursor.fetchall()) # Call the print_data function to print out all the game that filter by Main_Character based on user input in a table format
            Retry_Return("Select New Main Character?", "Return To Menu?", Print_MC_appeared_In, cursor)
        except: # If input is invalid or error, print Error
            print("Error")
        #End

def Print_Genre_filter(cursor): # Command 5 #Unique SQL
    print("") #Clean UI
    print("Select Genre Option") 
    cursor.execute(SQL_Code_Options("Genre_ID", "Genre", "Genre")) # Print out a list of Genre to select
    print_option(cursor.fetchall()) # Call the print_option function to print out the Genre to select
    print("Return = Return back to Menu") #UI for how to select Genre
    print("Finish = Finish selection") #UI for how to select Genre
    print("3 Selection max") #UI for how to select Genre
    Genre_1 = 0 # Variable to store Genre1 selection, default is 0 which is not a valid Genre_ID in database, so if user only select 1 Genre, it will only filter by Genre1 and ignore Genre2 and Genre3 since they are 0
    Genre_2 = 0
    Genre_3 = 0
    finish = "finish"
    return_menu = "return"
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
            print_data(cursor.fetchall()) # Call the print_data function to print out all the game that filter by Genre based on user input in a table format
            Retry_Return("Select New Genre?", "Return To Menu?", Print_Genre_filter, cursor)
    while True: # While True Loop to ask for Genre
            try: # Try Except to catch error or invalid input
                Selected_Genre = input("Select Genre: ") #Ask for Genre
                return_shortcut(Selected_Genre) # If user input return, it will return to Menu
                if Selected_Genre.lower() == finish: # If user select finish, it will filter by Genre1 which is 0, since there is no Genre with Genre_ID 0 in database, it will return empty result, and then it will ask for Genre again until user select a valid Genre or select return to Menu
                    filter_Genre(Genre_1, Genre_2, Genre_3, cursor)
                else:
                    Genre_1 = int(Selected_Genre) # Store the selected Genre in Genre1 variable
                    Selected_Genre2 = input("Select another Genre?: ") #Ask for Genre
                    return_shortcut(Selected_Genre2) # If user input return, it will return to Menu
                    if Selected_Genre2.lower() == finish:
                        filter_Genre(Genre_1, Genre_2, Genre_3, cursor)
                    else:
                        Genre_2 = int(Selected_Genre2)
                        Selected_Genre3 = input("Select Last Genre?: ") #Ask for Genre
                        return_shortcut(Selected_Genre3) # If user input return, it will return to Menu
                        if Selected_Genre3.lower() == finish:
                            filter_Genre(Genre_1, Genre_2, Genre_3, cursor)
                        else:
                            Genre_3 = int(Selected_Genre3)
                            filter_Genre(Genre_1, Genre_2, Genre_3, cursor)

            except: # If input is invalid or error, print Error
                print("Error")
        #End

def print_REL_filter(cursor): # Command 6 # Unique SQL
    print("") #Clean UI
    print("""
 _______________________________
|   Choose Date Filter Option   |
|_______________________________|
| 1 | = | Is Equal To           |
| 2 | = | Higher                |
| 3 | = | Lower                 |
| 4 | = | Higher OR Is Equal To |
| 5 | = | Lower OR Is Equal To  |
| 6 | = | Not Equal To          |
|___|___|_______________________|
|return = Return to Menu        |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾           
""")
    while True: # While True Loop to ask for Date
        try: # Try Except to catch error or invalid input
            Selected_Date = input("Filter: ") #Ask for Date
            return_shortcut(Selected_Date)
            if Selected_Date == "1":
                Selected_Date = "= " + input("Year: ")
            elif Selected_Date == "2":
                Selected_Date = "> " + input("Year: ")
            elif Selected_Date == "3":
                Selected_Date = "< " + input("Year: ")
            elif Selected_Date == "4":
                Selected_Date = ">= " + input("Year: ")
            elif Selected_Date == "5":
                Selected_Date = "<= " + input("Year: ")
            elif Selected_Date == "6":
                Selected_Date = "!= " + input("Year: ")
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
            print_data(cursor.fetchall()) # Call the print_data function to print out all the game that filter by Release Year based on user input in a table format
            Retry_Return("Select New Date?", "Return To Menu?", print_REL_filter, cursor)
        except: # If input is invalid or error, print Error
            print("Error")
        #End

def Print_All_Selected_Publisher(cursor): #Command 7
    print("") #Clean UI
    print(f"Select Publisher Option")
    cursor.execute(SQL_Code_Options("Publisher.Publisher_ID", "Publisher.Publisher", "Publisher")) # Excute the first SQL Code
    print_option(cursor.fetchall()) # Call the print_option function to print out the Publisher to select
    print("Return = Return back to Menu")
    while True: # While True Loop to ask for Publisher
         try:# Try Except to catch error or invalid input
            Selected_Publisher = input("Select Publisher: ") #Ask for Publisher
            return_shortcut(Selected_Publisher) # If user input return, it will return to Menu
            cursor.execute(SQL_Code_Selected_Data("Publisher.Publisher_ID", Selected_Publisher)) # Excute the second SQL Code
            print_data(cursor.fetchall()) # Call the print_data function to print out all game by selected Publisher in a table format
            Retry_Return("Select New Publisher?", "Return To Menu?", Print_All_Selected_Publisher, cursor)
         except:# If input is invalid or error, print Error
            print("Error")
              #End
                    
def Menu(Username):
    with sqlite3.connect(DATABASE) as db: # Connect to Database
          cursor = db.cursor() # Create Cursor
          print("""
                Type Command / h = Help / exit = Exit
 ____________________________________________________________________________
| 1 | = | Print All (Every Game Info in Database                             |
| 2 | = | Print All The Games Info From Selected Franchise                   |
| 3 | = | Print Info from Selected Game                                      |
| 4 | = | Print All Game & Info From The Selected Main Character Appeared In |
| 5 | = | Print All Game By Filter Genre                                     |
| 6 | = | Print Game By Specific Release date                                |
| 7 | = | Print All Game By Selected Publisher                               |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
""")
          while True:
              
                command = input(f'C:/User/{Username}>')
                if command.lower() == "help":
                    print("Help yourself")
                    Menu(Username)
                elif command.lower() == "exit":
                    break
                elif int(command) == 1:
                    Print_All(cursor)
                    Return_Menu()
                elif int(command) == 2:
                    Print_All_Selected_Franchise(cursor)
                elif int(command) == 3:
                    Print_Game_Info(cursor)
                elif int(command) == 4:
                    Print_MC_appeared_In(cursor)
                elif int(command) == 5:
                    Print_Genre_filter(cursor)
                elif int(command) == 6:
                    print_REL_filter(cursor)
                elif int(command) == 7:
                    Print_All_Selected_Publisher(cursor)
                else:
                    raise
            

if __name__ == "__main__":
    Skip_Loading = True
    Skip_Security_Check = True
    Load()
    Username = Security()
    Menu(Username)