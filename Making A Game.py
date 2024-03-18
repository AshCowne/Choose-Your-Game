# Programmer: Ash Cowne
# Date:3.15.2024
# Program: Make A Game

# first code before it broke

import time


def intro():
    print("Welcome, brave adventurer, to the Quest of the Lost Realm!\n")
    time.sleep(2)
    print("In this game, your choices will determine your fate.\n")
    time.sleep(2)
    print("Let the adventure begin!\n")
    time.sleep(2)


def crossroads():
    print("Chapter 1: The Crossroads\n")
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


def outcome():
    print("\nChapter 3: The Outcome\n")
    time.sleep(2)
    print("Your journey has come to an end, and your fate is sealed.\n")
    time.sleep(2)
    print(
        "Whether you emerged victorious or met your demise, your story will be remembered in the annals of history.\n")
    time.sleep(2)
    print("Thank you for playing the Quest of the Lost Realm!\n")


def main():
    intro()
    crossroads()
    choice = input("Your choice: ")

    if choice == "1":
        cave()
        cave_choice = input("Your choice: ")
        if cave_choice == "1":
            print("\nYou bravely face the dragon in combat, but alas, your efforts are in vain.")
            print("The dragon's fiery breath consumes you, and your adventure comes to a tragic end.\n")
        elif cave_choice == "2":
            print("\nYou attempt to flee from the dragon, but it swiftly catches up to you.")
            print("With a mighty roar, it engulfs you in flames, ending your journey in a blaze of glory.\n")
    elif choice == "2":
        treasure_path()
        treasure_choice = input("Your choice: ")
        if treasure_choice == "1":
            print("\nAs you open the chest, you're delighted to find it filled with gold and jewels.")
            print(
                "You've successfully claimed the hidden treasure and secured your place in history as a legendary adventurer!\n")
        elif treasure_choice == "2":
            print("\nYou decide to leave the chest untouched and continue on your journey.")
            print("Though you may never know what treasures it held, your quest continues.\n")
    elif choice == "3":
        brook()
        brook_choice = input("Your choice: ")
        if brook_choice == "1":
            print("\nYou take a moment to rest and refresh yourself by the waterfall.")
            print("Feeling rejuvenated, you continue on your journey with renewed vigor.\n")
        elif brook_choice == "2":
            print("\nYou press on with your journey without stopping.")
            print("The babbling brook fades into the distance as you forge ahead, eager to discover what lies ahead.\n")
    else:
        print("\nInvalid choice! Please select a valid option.\n")
        main()

    outcome()


if __name__ == "__main__":
    main()