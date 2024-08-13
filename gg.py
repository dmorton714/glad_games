import random
import time
import os
from intro import GameIntro

#Title screen of the game 
title_screen = (
        "Welcome to:\n"
        "\n  _____ _           _ _       _               _____                           _ "
        "\n |  __ \ |         | (_)     | |             |  __ \                         | | "
        "\n | |  \/ | __ _  __| |_  __ _| |_ ___  _ __  | |  \/ __ _ _ __ ___   ___  ___| | "
        "\n | | __| |/ _` |/ _` | |/ _` | __/ _ \| '__| | | __ / _` | '_ ` _ \ / _ \/ __| | "
        "\n | |_\ \ | (_| | (_| | | (_| | || (_) | |    | |_\ \ (_| | | | | | |  __/\__ \_| "
        "\n  \____/_|\__,_|\__,_|_|\__,_|\__\___/|_|     \____/\__,_|_| |_| |_|\___||___/(_)"
    )

intro = GameIntro(title_screen)
intro.start()

# Displays the characters and info
from characters import characters

from char_sel import Character
