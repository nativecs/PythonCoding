print("Random Rolling Dice Generator, have three dices")
askDice1 = int(input("How many sides for dice 1?: "))
askDice2 = int(input("How many sides for dice 2?: "))
askDice3 = int(input("How many sides for dice 3?: "))

import random
while True:
    def rollDice(dice1, dice2, dice3):
        dice1 = random.randint(1,askDice1)
        dice2 = random.randint(1,askDice2)
        dice3 = random.randint(1,askDice3)
        print("Dice 1 rolled is:", dice1)
        print("Dice 2 rolled is:", dice2)
        print("Dice 3 rolled is:", dice3)
    rollDice(askDice1, askDice2, askDice3)
    again = input("Do you want to roll again? Y or N?: ")
    if again == "N":
        print("Goodbye")
        break




