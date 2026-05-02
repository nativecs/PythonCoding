username = "joshua"
password = "apple123"
def login():
    userInput = input("Please enter your username: ")
    if userInput == username:
        print("Hello", username)
        askPass = input("Enter your password: ")
        if askPass == password:
            print("WELCOME TO REPLIT")
            return
    print("Invalid login")
    ask = input("Try again? Y or N: ")
    if ask.upper() == "Y":
        login()
    else:
        print("Goodbye")

login()

