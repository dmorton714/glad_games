import random
import time
import os

class GameIntro:
    def __init__(self, title, int_times=5):
        self.title_screen = title
        self.int_times = int_times
        self.loading_bar = [
            "  ------------------------------------------------------------------------------\n",
            "     ---------------------------------------------------------------------------\n",
            "            --------------------------------------------------------------------\n"
        ]

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def display_title(self):
        for _ in range(self.int_times):
            print(self.title_screen)
            time.sleep(0.25)
            self.clear_screen()
            time.sleep(0.125)
        print(self.title_screen)

    def display_loading_bar(self):
        for line in self.loading_bar:
            for char in line:
                print(char, end="", flush=True)
                time.sleep(0.009)  # wait for loading effect
            time.sleep(0.125)  # Wait for next line

    def start(self):
        self.display_title()
        self.display_loading_bar()
        input("Press Enter to Play")
        self.clear_screen()

# Usage
if __name__ == "__main__":
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
