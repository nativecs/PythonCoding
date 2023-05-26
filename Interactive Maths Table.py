ask = "Y"
counter = 0
while ask == "Y":
    print("Interactive Maths table")
    number = int(input("Enter your number: "))
    for table in range(1, 11):
        ask = int(input(f"What is {number} x {table} = ?: "))
        multple = number * table
        if ask == multple:
            counter += 1
            print(f"correct answer!, you've got",counter,"points")
        else:
            print("incorrect answer, 0 points")
    else:
        ask = input("Would you like to try again? Y or N?: ")
        if ask == "Y":
            continue
        else:
            break
print("Goodbye")

