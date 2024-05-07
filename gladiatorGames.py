characters = {
    "Fighter": [],
    "Mage": [],
    "Monk": [],
    "Citizen": []
}

def create_character(class_name, name):
    if class_name in characters:
        class_stats = {
            "Fighter": {"hp": 100, "mp": 50, "strength": 10, "agility": 5},
            "Mage": {"hp": 80, "mp": 100, "strength": 5, "agility": 8},
            "Monk": {"hp": 90, "mp": 60, "strength": 8, "agility": 10},
            "Citizen": {"hp": 120, "mp": 90, "strength": 10, "agility": 5}
        }
        character = {"name": name, "level": 1}
        character.update(class_stats[class_name])
        characters[class_name].append(character)
        print(f"{name} the {class_name} has been created!")
    else:
        print("Invalid character class.")

def main():
    print("Welcome to the character creation system!")
    print("Available character classes:")
    for class_name in characters:
        print("-", class_name)
    
    class_name = input("Choose a character class: ")
    if class_name in characters:
        name = input("Enter character name: ")
        create_character(class_name, name)
    else:
        print("Invalid character class.")

if __name__ == "__main__":
    main()
