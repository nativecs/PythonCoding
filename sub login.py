username = "joshua"
password = "apple123"
again = "Y"

def login():
  userInput = input("Please enter your username: ")
  if userInput == username:
    print("Hello", username)
    askPass = input("Enter your password: ")
    if askPass == password and username == username:
      print("WELCOME TO REPLIT")
  else:
    print("Invalid login")
    ask = input("Try again? Y or N: ")
    if ask != "Y":
        print("Goodbye")
    else:
        login()

login()

