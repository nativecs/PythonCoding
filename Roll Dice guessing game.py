import random
print("Infinity Dice 🎲")
sides = int(input("How many sides? "))
def rollDice(sides):
  while True:
    roll = random.randint(1,sides)
    print("You rolled", roll)
    again = input("Roll again? Y or N? ")
    print()
    if again == "N":
      print("goodbye")
      break
rollDice(sides)
