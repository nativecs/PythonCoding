print("welcome to the online grade checker")
while True:
    ask = input("Please enter the name of the subject: ")
    if ask == "Science" or ask == "Maths" or ask == "ICT" or ask == "English":
        grade = int(input(f"Please enter your marks obtained in {ask}: "))
        if grade >= 90 and grade <= 100:
            print(f"Your grade in {ask} is A+")
        elif grade >= 80 and grade <= 89:
            print(f"Your grade in {ask} is A")
        elif grade >= 70 and grade <= 79:
            print(f"Your grade in {ask} is B")
        elif grade >= 60 and grade <= 69:
            print(f"Your grade in {ask} is C")
        elif grade >= 50 and grade <= 59:
            print(f"Your grade in {ask} is D")
        elif grade <= 50:
            print(f"Your grade in {ask} is U")
    else:
        print("Invalid subject entered. Enter valid subject")
        repeat = input("Would you like to try again?, enter Y or N: ")
        if repeat == "Y":
            continue
        else:
            if repeat == "N":
                print("Goodbye")
                break
