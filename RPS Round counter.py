print("E P I C 🪨   📄  ✂️    B A T T L E ️ 🪨   📄  ✂️")
print()
print("Select R, P or S")
print("")
name1 = input("Enter 1st player name: ")
name2 = input("Enter 2nd player name: ")
player1score = 0
player2score = 0
round = 0
from getpass import getpass as input
again = "yes"
while again == "yes":
    round = round + 1
    print("")
    print("************Round", round,"************")
    print("")
    player1 = input("1st player, Enter your selection: ")
    player2 = input("2nd player, Enter your selection: ")
    if player1 == "R":
        if player2 == "R":
          print("") #add space for result
          print("You both smashed each other with 🪨, So its draw!!")
          print("")
          print(name1, "has", player1score, "points and", name2, "has",player2score,"points")
        elif player2 == "P":
          print("") #add space for result
          print(name1, "🪨 is smothered by", name2, "📄")
          player2score = player2score + 1
          print(name1, "has", player1score, "points and", name2, "has",player2score,"points")
        elif player2 == "S":
          print("") #add space for result
          print(name1, "🪨 has annihilated ", name2, "✂️")
          player1score = player1score + 1
          print(name1, "has", player1score, "points and", name2, "has",player2score,"points")
        else:
          print("") #add space for result
          print("Invalid Move!!")


    elif player1 == "P":
        if player2 == "P":
            print("")
            print("Two bits of 📄 flap at each other. Dissapointing. Draw!!")
            print(name1, "has", player1score, "points and", name2, "has",player2score,"points")
        elif player2 == "R":
            print("")
            print(name2, "🪨 is smothered by", name1, "📄")
            player1score = player1score + 1
            print(name1, "has", player1score, "points and", name2, "has",player2score,"points")
        elif player2 == "S":
            print("")
            print(name1, "📄 is cut into tiny pieces by", name2, "✂️")
            player2score = player2score + 1
            print(name1, "has", player1score, "points and", name2, "has",player2score,"points")
        else:
            print()
            print("Invalid Move!!")


    elif player1 == "S":
        if player2 == "S":
            print()
            print("Ka-Shing! ✂️ bounce off each other like a dodgy sword fight! Draw!!")
        elif player2 == "R":
            print()
            print("🪨 makes metal-dust out of", name1, "✂️")
        elif player2 == "P":
            print()
            print(name2, "📄 is cut into tiny pieces by", name1, "✂️")
        else:
            print()
            print("Invalid Move!!")

    else:
        print()
        print("Invalid Move!!")

    print()
    again = input("Do you want to play again: ")
    if player1score == 3 or player2score == 3:
      print("Max score of 3 achieved, thanks for playing")
      exit()

print()
print("See you soon 👋")