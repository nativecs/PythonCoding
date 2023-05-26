import random

print("⚔️ Character Stats Generator ⚔️")
print()

while True:
    def dice(sides):
        number = random.randint(1, sides)
        return number
    def player():
        roll1 = dice(6)
        roll2 = dice(8)
        health = roll1 * roll2
        return health

    gameHealth = player()

    character = input("Enter your character: ")
    print("The health of", character, "is", gameHealth, "hp")
    ask = input("Would you like to try again? Y or N: ")
    if ask == "N":
        print("Goodbye")
        break
    elif ask == "Y":
        continue
        exit()




