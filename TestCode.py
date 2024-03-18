# Programmer: Ash Cowne
# Date:3.15.2024
# Program: Make A Game

# first code before it broke


import time


class Character:
    def __init__(self, name, character_class, health, strength, agility):
        self.name = name
        self.character_class = character_class
        self.health = health
        self.strength = strength
        self.agility = agility

    def display_status(self):
        print("\n--- Status ---")
        print(f"Name: {self.name}")
        print(f"Class: {self.character_class}")
        print(f"Health: {self.health}")
        print(f"Strength: {self.strength}")
        print(f"Agility: {self.agility}\n")


def intro():
    print("Welcome, brave adventurer, to the Quest of the Lost Realm!\n")
    time.sleep(2)
    print("In this game, your choices will determine your fate.\n")
    time.sleep(2)
    print("Let the adventure begin!\n")
    time.sleep(2)


def choose_class():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Rogue")
    print("3. Mage")
    choice = input("Your choice: ")
    classes = {
        "1": ("Warrior", 100, 10, 5),
        "2": ("Rogue", 80, 8, 10),
        "3": ("Mage", 70, 5, 12)
    }
    return classes.get(choice, ("Adventurer", 90, 7, 7))  # Default to Adventurer class if choice is invalid


def crossroads(character):
    print("\nChapter 1: The Crossroads\n")
    time.sleep(2)
    print("You find yourself standing at a crossroads in the heart of the forest.\n")
    time.sleep(2)
    print("To the north lies a dark and ominous cave, rumored to be the lair of a fearsome dragon.\n")
    time.sleep(2)
    print("To the east, a narrow path leads deeper into the woods, where whispers speak of hidden treasure.\n")
    time.sleep(2)
    print("To the west, a babbling brook winds its way through the trees, its waters sparkling in the sunlight.\n")
    time.sleep(2)
    print("Which path will you choose?\n")
    time.sleep(1)
    print("1. Venture into the cave to face the dragon.")
    print("2. Follow the narrow path in search of treasure.")
    print("3. Follow the brook and see where it leads.\n")


def cave():
    print("\nChapter 2: The Dragon's Lair\n")
    time.sleep(2)
    print("You enter the cave, its darkness enveloping you like a thick cloak.\n")
    time.sleep(2)
    print("As you cautiously make your way deeper into the cavern, you hear a low growl echoing off the walls.\n")
    time.sleep(2)
    print("Suddenly, the dragon appears before you, its scales glinting in the dim light.\n")
    time.sleep(2)
    print("What will you do?\n")
    time.sleep(1)
    print("1. Stand your ground and prepare to fight.")
    print("2. Attempt to flee from the dragon.")


def treasure_path():
    print("\nChapter 2: The Hidden Treasure\n")
    time.sleep(2)
    print("You follow the narrow path, the trees growing thicker around you with each step.\n")
    time.sleep(2)
    print("After what feels like hours of walking, you stumble upon a clearing.\n")
    time.sleep(2)
    print("In the center of the clearing, you see a chest, its lid slightly ajar.\n")
    time.sleep(2)
    print("Do you dare to open it?\n")
    time.sleep(1)
    print("1. Open the chest and see what treasures lie within.")
    print("2. Leave the chest untouched and continue on your journey.")


def brook():
    print("\nChapter 2: The Babbling Brook\n")
    time.sleep(2)
    print("You follow the babbling brook as it winds its way through the forest.\n")
    time.sleep(2)
    print("The sound of running water is soothing, and you feel a sense of peace wash over you.\n")
    time.sleep(2)
    print("Suddenly, you come across a small waterfall, its waters cascading into a crystal-clear pool below.\n")
    time.sleep(2)
    print("Will you take a moment to rest and refresh yourself?\n")
    time.sleep(1)
    print("1. Take a break and enjoy the tranquility of the waterfall.")
    print("2. Press on with your journey without stopping.")


def dragon_fight():
    print("\nChapter 3: The Dragon's Defeat\n")
    time.sleep(2)
    print("You bravely face the dragon in combat, dodging its fiery breath and striking back with all your might.\n")
    time.sleep(2)
    print("After a fierce battle, you emerge victorious, the dragon lying defeated at your feet.\n")
    time.sleep(2)
    print(
        "With the dragon slain, you claim its hoard of treasures as your own, cementing your place as a legendary hero!\n")


def dragon_flee():
    print("\nChapter 3: A Narrow Escape\n")
    time.sleep(2)
    print("You attempt to flee from the dragon, your heart pounding in your chest as you run for your life.\n")
    time.sleep(2)
    print("Miraculously, you manage to outrun the beast and escape the cave, albeit with a few singed hairs.\n")
    time.sleep(2)
    print(
        "Though you may have avoided certain death, the memory of the dragon's fury will haunt your dreams for years to come.\n")


def open_treasure():
    print("\nChapter 3: Riches Beyond Measure\n")
    time.sleep(2)
    print(
        "As you open the chest, you're delighted to find it filled with gold, jewels, and other priceless artifacts.\n")
    time.sleep(2)
    print(
        "You've successfully claimed the hidden treasure and secured your place in history as a legendary adventurer!\n")


def ignore_treasure():
    print("\nChapter 3: The Road Less Taken\n")
    time.sleep(2)
    print("You decide to leave the chest untouched and continue on your journey.\n")
    time.sleep(2)
    print("Though you may never know what treasures it held, your quest continues.\n")


def rest_at_waterfall():
    print("\nChapter 3: Renewed Vigor\n")
    time.sleep(2)
    print("You take a moment to rest and refresh yourself by the waterfall.\n")
    time.sleep(2)
    print("Feeling rejuvenated, you continue on your journey with renewed vigor.\n")


def continue_without_rest():
    print("\nChapter 3: The Journey Continues\n")
    time.sleep(2)
    print("You press on with your journey without stopping.\n")
    time.sleep(2)
    print("The babbling brook fades into the distance as you forge ahead, eager to discover what lies ahead.\n")


def dragon_victory():
    print("\nChapter 4: The Conqueror\n")
    time.sleep(2)
    print("Having defeated the dragon and claimed its hoard, you return to the village as a conquering hero.\n")
    time.sleep(2)
    print("The villagers hail you as their savior, and your name is forever etched into the annals of history.\n")


def treasure_hunter():
    print("\nChapter 4: The Treasure Hunter\n")
    time.sleep(2)
    print("With the hidden treasure in your possession, you journey to distant lands in search of more riches.\n")
    time.sleep(2)
    print("Your adventures take you to places beyond imagination, and tales of your exploits spread far and wide.\n")


def nature_seekers():
    print("\nChapter 4: The Nature Seekers\n")
    time.sleep(2)
    print("Having spent time in nature's embrace, you develop a deep appreciation for the beauty of the world.\n")
    time.sleep(2)
    print("You become a protector of the forest, ensuring that its wonders remain untouched for generations to come.\n")


def main():
    intro()
    name = input("Enter your character's name: ")
    character_class, health, strength, agility = choose_class()
    player = Character(name, character_class, health, strength, agility)
    player.display_status()

    crossroads(player)
    choice = input("Your choice: ")

    if choice == "1":
        cave()
        cave_choice = input("Your choice: ")
        if cave_choice == "1":
            dragon_fight()
            dragon_victory()
        elif cave_choice == "2":
            dragon_flee()
            treasure_hunter()
    elif choice == "2":
        treasure_path()
        treasure_choice = input("Your choice: ")
        if treasure_choice == "1":
            open_treasure()
            treasure_hunter()
        elif treasure_choice == "2":
            ignore_treasure()
            nature_seekers()
    elif choice == "3":
        brook()
        brook_choice = input("Your choice: ")
        if brook_choice == "1":
            rest_at_waterfall()
            nature_seekers()
        elif brook_choice == "2":
            continue_without_rest()
            treasure_hunter()
    else:
        print("\nInvalid choice! Please select a valid option.\n")
        main()


if __name__ == "__main__":
    main()
