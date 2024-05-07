BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m' # orange on some systems
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
LIGHT_GRAY = '\033[37m'
DARK_GRAY = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
WHITE = '\033[97m'

RESET = '\033[0m' # called to return to standard terminal text color

print(BLACK + "black" + RESET)
print(RED + "red" + RESET)
print(GREEN + "green" + RESET)
print(YELLOW + "yellow" + RESET)
print(BLUE + "blue" + RESET)
print(MAGENTA + "magenta" + RESET)
print(CYAN + "cyan" + RESET)
print(LIGHT_GRAY + "light gray" + RESET)
print(DARK_GRAY + "dark gray" + RESET)
print(BRIGHT_RED + "bright red" + RESET)
print(BRIGHT_GREEN + "bright green" + RESET)
print(BRIGHT_YELLOW + "bright yellow" + RESET)
print(BRIGHT_BLUE + "bright blue" + RESET)
print(BRIGHT_MAGENTA + "bright magenta" + RESET)
print(BRIGHT_CYAN + "bright cyan" + RESET)
print(WHITE + "white" + RESET)


#-----------------------------------------
    #color map working
#-----------------------------------------



mage = '''
                                                @@@@@@@
                                             @@%::::::@@
                                       @@@@@@@%::::::@@
                                      @@+::::::::-===@@
                                    @@@+::::::::-===@@
                               @@@@@@@-::::::::-==*@@
                             @@======-:::::----==*@@
                         @@@@@@::::::::::::-=====*@@
                      @@@@:::::::::::::::-=====+@@@
      @@@@@@@@@@@@@@@@@@@:::::::::-------=====+@@
    @@::::::::::::::::::::::::::::============+@@
       @@*============:::::::::::::::=========+@@
       @@*============:::::::::::::::=========+@@
          @@@@@@@@%===============-::::::::#@@
                @%===============---------#@@
                  @@@@@@@@@@==================+@@
                @%===@@@@@@@@@@@@@@@==========++#@@
                @#::-@@@@@@@@@@@@@@@============*@@
                @#::-@@@@@@:::@@@@@@@@@@@@*=========@@
                @#::-@@@@@@:::@@@@@@@@@@@@*=========@@
      @@@@@@#**#@@@@@@@@@@@@:::@@@@@@@@@@@@*==+@@%=====+@@
      @@@%**@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@**#@@
      @@@%**@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@**#@@
      @@@%********#@@@@@@@@@*********************#@@
      @@@%##******#@@@@@@@@@***#########*******##%@@
      @@@@@@@#***++++++*********@@@@@@@@@#+++++*@@
    @@------%@@%+++++++++@@@@@@*********+++++++**#@@
    @@::::::%@@@+++++++++@@@@@@++++++++++++++++++#@@
    @@::::::%@@@++++++@@@@@@@@@++++++++++++++++++#@@
    @@::::::%@@@++++++@@@@@@@@@++++++++++++++++++#@@
    @@@@@@@@*+++++++++::::::@@@++++++++++++++++++#@@
    @@@@@%**@@@%++++++::::::@@@++++++++++++++++++#@@
     @@@@%**@@@@++++++::::::@@@++++++++++++++++++#@@
       @@%**@@@@++++++@@@@@@@@@+++++++++++++++*@@
       @@%**%@@%**++++@@@@@@@@@***++++++++++++*@@
       @@%*****#@@%++++++++++++@@@++++++++++++*@@
       @@%********%@@@+++++++++@@@++++++++++++*@@
       @@%********#@@@+++++++++@@@++++++++++++*@@
       @@%************@@@@@@++++++@@@++++++%@@@**#@@
       @@%************@@@@@@++++++@@@++++++%@@@**#@@
    @@*************************++++++@@@@@@#*********@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
'''





def colorAscii(artwork, color_map):
    COLOR_CODES = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'bright_black': '\033[90m',
        'bright_red': '\033[91m',
        'bright_green': '\033[92m',
        'bright_yellow': '\033[93m',
        'bright_blue': '\033[94m',
        'bright_magenta': '\033[95m',
        'bright_cyan': '\033[96m',
        'bright_white': '\033[97m',
        'reset': '\033[0m'
    }
    for line in artwork.split('\n'):
        for letter in line:
            if letter.lower() in color_map:
                color = color_map[letter.lower()]
                color_code = COLOR_CODES.get(color, '')
                print(f"{color_code}{letter}{COLOR_CODES['reset']}", end='')
            else:
                print(letter, end='')
        print()

# Mage color map 
mageMap = {
    '@': 'black',
    '%': 'bright_blue',
    ':': 'bright_yellow',
    '+': 'blue',
    '*': 'bright_blue',
    '-': 'yellow',
    '=': 'yellow',
    '#': 'blue',
}

# Call the function with the artwork and color mappings
colorAscii(mage, mageMap)

