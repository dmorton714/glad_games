class Character:
    all_characters = {
        "Fighter": [],
        "Mage": [],
        "Monk": [],
        "Citizen": []
    }

    class_stats = {
        "Fighter": {"hp": 100, "mp": 50, "strength": 10, "agility": 5},
        "Mage": {"hp": 80, "mp": 100, "strength": 5, "agility": 8},
        "Monk": {"hp": 90, "mp": 60, "strength": 8, "agility": 10},
        "Citizen": {"hp": 120, "mp": 80, "strength": 9, "agility": 5}
    }

    def __init__(self, name, class_name):
        if class_name in Character.class_stats:
            self.name = name
            self.class_name = class_name
            self.level = 1
            self.stats = Character.class_stats[class_name].copy()
            Character.all_characters[class_name].append(self)
            print(f"{self.name} the {self.class_name} has been created!")
        else:
            raise ValueError("Invalid character class.")

    @classmethod
    def create_character(cls, class_name, name):
        return cls(name, class_name)


def main():
    while True:
        print("Please create a character! \n")
        print("Available character classes:")
        for i, class_name in enumerate(Character.all_characters, 1):
            print(f"{i}. {class_name}")

        class_index = input("Choose a character class (by'#'): ")
        try:
            class_index = int(class_index)
            if 1 <= class_index <= len(Character.all_characters):
                class_name = list(Character.all_characters.keys())[class_index - 1]
                while True:
                    name = input("Enter character name: ")
                    if name.strip():
                        current_char = Character.create_character(class_name, name)
                        return  # Exit the function if a valid name is entered
                    else:
                        print("Name cannot be blank.")
            else:
                print("Invalid character class number.")
        except ValueError:
            print("Please enter a valid number.")


main()
