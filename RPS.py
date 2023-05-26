print("E P I C 🪨   📄  ✂️    B A T T L E ️ 🪨   📄  ✂️")
print()
print("Select R, P or S")
name1 = input("Enter 1st player name: ")
name2 = input("Enter 2nd player name: ")

again = "yes"
while again == "yes":
    print()
    player1 = input("1st player, Enter your selection: ")
    player2 = input("2nd player, Enter your selection: ")

    if player1 == "R":
        if player2 == "R":
            print()
            print("You both smashed each other with 🪨, So its draw!!")
        elif player2 == "P":
            print()
            print(name1, "🪨 is smothered by", name2, "📄")
        elif player2 == "S":
            print()
            print(name1, "🪨 has annihilated ", name2, "✂️")
        else:
            print()
            print("Invalid Move!!")


    elif player1 == "P":
        if player2 == "P":
            print()
            print("Two bits of 📄 flap at each other. Dissapointing. Draw!!")
        elif player2 == "R":
            print()
            print(name2, "🪨 is smothered by", name1, "📄")
        elif player2 == "S":
            print()
            print(name1, "📄 is cut into tiny pieces by", name2, "✂️")
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

print()
print("See you soon 👋")