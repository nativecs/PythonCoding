import random
import time
import os


def dice(sides):
    throw = random.randint(1, sides)
    return throw


def health():
    player1 = dice(6)
    player2 = dice(12)
    health = (player1 * player2) / 2 + 10
    health = round(health)
    return health


gameHealth = health()


def strength():
    player1 = dice(6)
    player2 = dice(12)
    strength = (player1 * player2) / 2 + 12
    strength = round(strength)
    return strength


gameStrength = strength()

print("👾👾👾👾 Character Builder 👾👾👾👾")
print()
time.sleep(1)
print("🎎🎎🎎🎎 VIDEO GAME MENU 🎎🎎🎎🎎")
time.sleep(1)
print()

counter = 0

while True:
    print("Select your character type")
    print()
    time.sleep(0.3)
    print("Human\nElf\nWiard\nOrc")
    time.sleep(0.3)
    print()
    menu = input("🤖 Name your Legend: ")
    if menu == "Human" or menu == "Elf" or menu == "Wiard" or menu == "Orc":
        askHuman = input("\nName your character: ")
        askSex = input(f"What gender is {askHuman} M of F: ")
        if askSex == "F" and askHuman == askHuman:
            counter = counter + 1
            print(f"\nall hail! {askHuman}!\nHealth is", gameHealth, "\n""Strength is", gameStrength)
            print("Characters Generated:", counter)

        elif askSex == "M" and askHuman == askHuman:
            counter = counter + 1
            print(f"\nBravo!{askHuman}!\nHealth is", gameHealth, "\n""Strength is", gameStrength)
            print("Characters Generated:", counter)
        if counter != 0:
            try1 = input("Would you like to generate another character? Y or N: ")
            if try1 == "Y":
                continue
            elif try1 == "N":
                print("\nTotal Characters generated:", counter)
                print("Goodbye!")
                time.sleep(0.5)
                os.system("clear")
                exit()
    else:
        print("You have an invalid character")
        time.sleep(0.3)
        os.system("clear")
        break
