import numpy
import random
import pprint
import time
import os

#---------------------------------------------------------------------
    # **** Welcome Screen ****** 
#---------------------------------------------------------------------

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

titleScreen = "Welcome to:\n\
\n  _____ _           _ _       _               _____                           _ \
\n |  __ \ |         | (_)     | |             |  __ \                         | | \
\n | |  \/ | __ _  __| |_  __ _| |_ ___  _ __  | |  \/ __ _ _ __ ___   ___  ___| | \
\n | | __| |/ _` |/ _` | |/ _` | __/ _ \| '__| | | __ / _` | '_ ` _ \ / _ \/ __| | \
\n | |_\ \ | (_| | (_| | | (_| | || (_) | |    | |_\ \ (_| | | | | | |  __/\__ \_| \
\n  \____/_|\__,_|\__,_|_|\__,_|\__\___/|_|     \____/\__,_|_| |_| |_|\___||___/(_)"

num_repetitions = 5

for _ in range(num_repetitions):
    print(titleScreen)
    time.sleep(0.25)
    clear_screen()
    time.sleep(0.125)

print(titleScreen)
loading_bar = [
    "  ------------------------------------------------------------------------------\n",
    "     ---------------------------------------------------------------------------\n",
    "            --------------------------------------------------------------------\n"
]


for line in loading_bar:
    for char in line:
        print(char, end="", flush=True)  
        time.sleep(0.009)  # Adjust the sleep time to control the speed of the loading effect
    time.sleep(0.125)  # Wait for next line

input("Press Enter to Play")
os.system('cls' if os.name == 'nt' else 'clear')



#---------------------------------------------------------------------
    # **** This will be where the game starts ****** 
#---------------------------------------------------------------------

# print("\nPress Enter to play the game or Esc to exit.")

# while True:
#     key = input()  
#     if key == '': #< enter key
#         print("Starting the game...")
#         # Add your game logic here
#         break
#     elif key == '\x1b':  #<esc key
#         print("Exiting the program...")
#         exit()


#---------------------------------------------------------------------
     # Dice roll with rolls on d20 
#---------------------------------------------------------------------

# # Define the dice graphic
# diceGraphic = "\n\
#    ^\n\
#  /_|_\\\n\
# |/{roll:2d}\ |\n\
#  \ | /\n\
#    v"

# def roll_stats(num_stats=5, num_sides=20):
#     stats = {}
#     for i in range(1, num_stats + 1):
#         stat = random.randint(1, num_sides)
#         stats[f"Roll {i}"] = stat
#     return stats

# # Generate a set of 5 stats (20-sided dice)
# stats = roll_stats()
# print("Character Stats Roll:")
# for roll, value in stats.items():
#     print(f"{roll}:")
#     print(diceGraphic.format(roll=value))

#---------------------------------------------------------------------
     # Character Lore and stats
#---------------------------------------------------------------------

fighterLore = '''In a future where survival demands strength above all else, 
fighters embody raw power and resilience. They are forged in the crucible of 
relentless combat, their instinct and physical might unmatched. While not 
known for their intellect, their unyielding spirit and thunderous blows 
inspire both fear and admiration. In this world of perpetual struggle, 
fighters stand as the vanguard of humanity's fight for survival, 
where only the strongest endure. \n'''

mageLore = '''In the futuristic realm where knowledge is power, mages harness
 the arcane energies of the universe to manipulate reality itself. Masters of 
 the mystic arts, they wield their spells with precision and finesse, 
 unraveling the secrets of the cosmos to reshape the world to their will. Though 
 physically frail, their minds are their greatest weapons, capable of unlocking 
 the boundless potential of magic to overcome any obstacle. \n'''

monkLore = '''Amidst the turmoil of the future, monks are beacons of spiritual 
enlightenment and martial prowess. Embracing discipline and inner strength, 
they walk the path of harmony and balance, seeking to unite mind, body, and 
soul. Through rigorous training and unwavering devotion, they achieve a state 
of martial perfection, capable of unleashing devastating strikes with unmatched 
speed and precision. \n'''

citizenLore = '''Once among the privileged few of society, the elite now find 
themselves cast into the crucible of the future's brutal arena. Born into wealth 
and privilege, they once wielded influence and power with impunity, but a single 
misstep has led them to the ultimate test of survival. Now, stripped of their 
opulent trappings and forced to confront the harsh realities of the world they 
once ignored, they must rely on their cunning and charm to navigate the deadly 
games that await. \n'''


classStats = {
            "Fighter": {"hp": 100, "mp": 50, "strength": 10, "agility": 5},
            "Mage": {"hp": 80, "mp": 100, "strength": 5, "agility": 8},
            "Monk": {"hp": 90, "mp": 60, "strength": 8, "agility": 10},
            "Citizen": {"hp": 120, "mp": 80, "strength": 9, "agility": 5}
        }


#---------------------------------------------------------------------
     # Character images  
#---------------------------------------------------------------------


fighter = '''FIGHTER \n
          @@   @@   @@@@@@@@@@@@@@@@@@@@  
       -=-++==-++-=-++++++++++++++++++++-= 
       @@+--@@+--#@@--------------------+@@  
    +@@--+@@-----------------------@@@@@@@@@@   
    +@@--------------------------------------+@@  
       +++------------------------------+++++.    
       @@+------------------------------+@@@@     
    +@@------------------------------------@@     
    +@@--+@@--    -=@@@@@--------------------+@@  
    +@@--+@@--   .=+@@@%%---------------======##  
    +@@--+@@--+@@@@@@@   ---------------+@@@@     
       @@   @@:  %@@     -----     .-------@@     
            @@-  %@@        --     .----+**       
            @@-  %@@        --     .----+@@       
          @@@@-               .----@@@@@@@@       
       @@   --              @@@@+-----   --@@     
       *#   --              @@##+-----   --**     
    +@@-------+@@        @@@@@=--------------+@@  
       @@+----+@@@@@@@@@@--+@@=--------------+@@  
     +=   -----==@@@@@+==---==#%         %%%%     
    +@@   -------%@@@@=-------@@         @@@@     
    +@@     @@*------------      @@=--     @@     
    +@@-----   --%@@@@=--          .----   @@     
               +++++++=--          :----   @@     
  @@        @@@@@=-------        ----------@@     
  @@        @@@@@=------------@@@@@@@@@@@@@       
    :@@@@@@@     +@#----------@@                  
    +@@@@@@@     *@@----------@@                  
                 *@@             @@               
                 *@@------------+@@               
                 *@@------------+@@               
                 *@@------------+@@               
                 *@@------------+@@               
               @@=--------------+@@               
               ++================++               
                 *@@@@@@@@@@@@@@  
'''

mage = '''MAGE
############################################################
###############################################%%%%%%%######
###############################################%@@@@@@######
#########################################@@@@@@=::::::@@@###
#########################################@@@@@@=......@@@###
#####################################%@@@..........::-@@@###
#####################################%@@@..........::-@@@###
###############################%@@@@@@..........::+@@@######
#########################%%%%%%#*****+..........::+@@@######
#######################@@@@@@=............::::::+@@@######
######@@@@@@@@@@@@@@@@@@@................::::::*@@%#########
######@@@@@@@@@@@@@@@@@@@................::::::*@@%#########
###@@@:............................::::::::::::*@@%#########
###@@@-::..........................::::::::::::*@@%#########
######@@@*::::::::::::................:::::::::*@@%#########
######%%%%#########::::::::::::::::.........*##%%%%#########
#########%@@@@@@@@@::::::::::::::::.........#@@%############
###################@@@@@@@@@*::::::::::::::::::*@@%#########
###################@@@@@@@@@#::::::::::::::::::+@@%#########
###############%@@@...#@@@@@@@@@@@@@@@::::::::::::+@@@######
############%@@@@@@...#@@@@@*..+@@@@@@%%%%%%-:::::----@@@###
############%@@@@@@...#@@@@@*..=@@@@@@@@@@@@-::::::::-@@@###
#########%@@#===@@@@@@@@@@@@*..=@@@@@@@@@@@@-::*@@+:::::-@@@
#########%@@#===@@@@@@@@@@@@*..=@@@@@@@@@@@@-::*@@+:::::-@@@
######@@@#==+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*==*@@@@@@###
######@@@#==+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*==*@@@@@@###
######@@@#=========@@@@@@@@@#=====================*@@@######
######@@@@@@#===------=========*@@@@@@@@@------*@@%#########
######@@@@@@#===------=========*@@@@@@@@@------*@@%#########
###@@@:.....-@@%---------@@@@@@+------------------*@@@######
###@@@:.....-@@%-------==@@@@@@+------------------*@@@######
###@@@:.....-@@%------%@@@@@@@@+------------------*@@@######
###%%%######*===------::::::=@@+------------------*@@@######
######@@@@@@#---------......-@@+------------------*@@@######
######@@@#==+@@%------......-@@+------------------*@@@######
######@@@#==+@@%------......-@@+------------------*@@@######
######@@@#==+@@%------%@@@@@@@@+---------------*@@%#########
######@@@#===******---=++++++++****------------*@@%#########
######@@@#======@@@------------*@@@------------*@@%#########
######@@@#=========@@@---------*@@@------------*@@%#########
######@@@#=========@@@---------*@@@------------*@@%#########
######@@@#============%@@@@@#------@@@------%@@*==*@@@######
###%%%%%%*============%%%%%%*------%%%------#%%*==*%%%%%%###
###@@@+========================-------@@@@@@+=========@@@###
###%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%###
######@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@######@@@@@@@@@@######'''
mage = mage.replace("#", " ")

monk = '''MONK
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@#++++++++++++++++++@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@+++++++++++++++++++++++*@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@#*#************************@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@*+++++++++++++++++++++++++*@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@%+++++++++++++++++++++++++++++++%@@@@@@@@@@@@@
@@@@@@@@@@@@@%++*++--+++*++++*++++*++*++*+*++%@@@@@@@@@@@@@
@@@@@@@@@@@@@%++*++--+++*++++*++++*++*++*+*++%@@@@@@@@@@@@@
@@@@@@@@@@@@@%+++++==+=====+++++=====+=====++%@@@@@@@@@@@@@
@@@@@@@@@@@@@%++++*@@@@@@@@--=+++++++++++++++%@@@@@@@@@@@@@
@@@@@@@@@@@@@@***+*@@@@@@@@=-+++++*++*++*+*++%@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@*++--%@@=----=+++++++++++++++%@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@--%@@=----=+++++++++++++++%@@@@@@@@@@@@@
@@@@@@@@@@@@@@%%%%%--#%%=--=-==+++*++*++*+*++%@@@@@@@@@@@@@
@@@@@@@@++*++*--+==-------------+++++++++++==%@@@@@@@@@@@@@
@@@@@@@@--=--*+++=+----------*@@---++++++==--+--@@@@@@@@@@@
@@@@@@@@--=--*+++=+===--=--#####+=+++*+++=+--+--###@@@@@@@@
@@@@@@@@--=--*+++=====-----@@#--=====+===----+--=--@@@@@@@@
@@@@@@@@++*++*+++====%@@@@@--========+==++++++--=--@@@@@@@@
@@@@@@@@@@@@@@@@%%%==****+*+=+==*+*++*==+====*==+--@@@@@@@@
@@@@@@@@@@@@@@@@@@@==+==---===--++++++-------+++=--@@@@@@@@
@@@@@@@@@@@@@@@@@@@==+=====--------+++++=----+--+++@@@@@@@@
@@@@@@@@@@@@@@@@@@@==+==+=+=-=----=++*++=-=--*++@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@==+=====--------+++++=----+++@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#--++++++----=@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@==+==@@@+=+=++=+==+==+=+@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@==+==@@@==+====+==+==+=+@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@==+==@@@==========+==@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@*===============+==@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@#+++++++++++++++*++@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@*===============*@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@+============*@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@%%+++++++++++++#@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@*===============*@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
'''
monk = monk.replace("@", " ")

citizen = '''CITIZEN
                                                           
                                   @@@@@@@@@: @@@@@@@@@-   
                             +@@@@@#########@@         #@: 
                           -@#################   :@@@@@-   
                           -@###############:      -@@@@@: 
                           -@#############=     ##@@@####@@
                           -@#############=   #########%@: 
                         .@%##########################@-   
                      @@@@######################@@##@+     
                    #@#############@@@@@@@@@@@@@ :@#       
@@@@@*                @@@@@@@@@@@@@-----:        :@#       
@@---*@=                   -@*-#@=------:          -@+     
@@::---#@:                 -@*-#@=------:            +@-   
 .@%::---@@                -@*----------:              #@: 
   :@#::---@@@@@*       @@@@@*----------:              #@: 
     =@+::-####@*     @@####@*----------:              #@: 
       *@####@%     #@######@##########-:     #### :###%@: 
       *@##@@#%@*   #@@@@@@@@@@@@######@* *@: #### :###%@: 
       *@@@  @@#%@=   @@@@@@@@@@@@@@@@@@@@@@###########%@: 
              :@@#@@@@-----+@########@%---#@###########%@: 
                =@@@@@-----+@@@@@@@##@%-----%@##@@@@@##%@: 
                    #@-----+@@@@@@@##@%-----%@##@@@@@##%@: 
                      @@@@@@@@@@@@@##@@@@@@@####@@@@@##%@: 
                        @@##@@@@@@@###########@@@@@@@##%@: 
                        @@##@@@@@@@           @@@@@@@##%@: 
                        @@##@@@@@@@###########@@@@@@@##%@: 
                        @@##@@@@@@@###########@@@@@@@##%@: 
                        @@#######@@###########@@#######%@: 
                         .@@@@@@@#############@@@@@@@@@@@: 
                                 %@@@@@@@@@@@@             
'''


print("Welcome to the character creation system!")

characterData = [
    (fighter, fighterLore, classStats["Fighter"]),
    (mage, mageLore, classStats["Mage"]),
    (monk, monkLore, classStats["Monk"]),
    (citizen, citizenLore, classStats["Citizen"])]

for character, characterLore, stats in characterData:
    print(character)
    print(characterLore)
    print("Stats:")
    for key, value in stats.items():
        print(f"{key}: {value}")
    input("Press Enter to see next class")
    os.system('cls' if os.name == 'nt' else 'clear')

# input("Press Enter to pick make your character")
# os.system('cls' if os.name == 'nt' else 'clear')

#---------------------------------------------------------------------
     # Character Selection screen 
#---------------------------------------------------------------------

# will store all characters created 
characters = {
    "Fighter": [],
    "Mage": [],
    "Monk": [],
    "Citizen": []
}

# Define currentChar globally to access later
currentChar = None  

def create_character(class_name, name):
    global currentChar  
    if class_name in characters:
        classStats = {
            "Fighter": {"hp": 100, "mp": 50, "strength": 10, "agility": 5},
            "Mage": {"hp": 80, "mp": 100, "strength": 5, "agility": 8},
            "Monk": {"hp": 90, "mp": 60, "strength": 8, "agility": 10},
            "Citizen": {"hp": 120, "mp": 80, "strength": 9, "agility": 5}
        }
        character = {"name": name, "level": 1}
        character.update(classStats[class_name])
        characters[class_name].append(character)
        print(f"{name} the {class_name} has been created!")
        currentChar = character  
        return character
    else:
        print("Invalid character class.")

def main():
    global currentChar  

    while True:
        print("Please create a character! \n")
        print("Available character classes:")
        for i, class_name in enumerate(characters, 1):
            print(f"{i}. {class_name}")

        class_index = input("Choose a character class (enter the corresponding number): ")
        try:
            class_index = int(class_index)
            if 1 <= class_index <= len(characters):
                class_name = list(characters.keys())[class_index - 1]
                while True:
                    name = input("Enter character name: ")
                    if name.strip():  # Check if the name is not blank after stripping whitespace
                        currentChar = create_character(class_name, name)
                        return  # Exit the function if a valid name is entered
                    else:
                        print("Name cannot be blank.")
            else:
                print("Invalid character class number.")
        except ValueError:
            print("Please enter a valid number.")

main()


#---------------------------------------------------------------------
     # Dice roll function and saves rolls to dict that
     # you define.
#---------------------------------------------------------------------

# Define the dice graphic
diceGraphic ="\n\
        _-_.  \n\
     _-',^. `-_.  \n\
 ._-' ,'   `.   `-_  \n\
!`-_._________`-':::  \n\
!   /\        /\::::  \n\
;  /  \ {roll:2d}   /..\:::  \n\
! /    \    /....\::  \n\
!/      \  /......\:  \n\
;--.___. \/_.__.--;;   \n\
 '-_    `:!;;;;;;;'  \n\
    `-_, :!;;;''  \n\
        `-!'    \n"

def rollDice(stats_dict, num_stats=5, num_sides=20):
    stats = {}
    for i in range(1, num_stats + 1):
        stat = random.randint(1, num_sides)
        stats[f"Roll {i}"] = stat
    stats_dict.update(stats)
    print("Character Stats Roll:")
    for roll, value in stats.items():
        print(f"{roll}:")
        print(diceGraphic.format(roll=value))


# Example usage:
# my_stats = {}
# rollDice(my_stats)

# print(my_stats)

#---------------------------------------------------------------------
     # Rolls Characters stats
#---------------------------------------------------------------------

# print(characters)
for key, value in currentChar.items():
    print(f"{key}: {value}")
    
input("Press Enter to roll level 1 stats")

# rolling stats
my_stats = {}

rollDice(my_stats)

for key, value in my_stats.items():
    print(f"{key}: {value}")
