ask = "Y"
while ask == "Y":
    print("Interactive Maths table")
    number = int(input("Enter your number: "))
    for table in range(1, 11):
        print(number, "x", table, "=", number * table)
    else:
        ask = input("Would you like to try again? Y or N?: ")
        if ask == "Y":
            continue
        else:
            break
print("Goodbye")


