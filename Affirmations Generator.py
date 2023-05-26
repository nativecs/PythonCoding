print("********Random affirmations generator********")
print("***This program will display a positive message based on your chosen day***")
print("\n")
name = input("Please enter your name: ")
print("Hi",name,"nice to meet you")
dayOfWeek = input("What is the current day of the week? ")
if dayOfWeek == "Monday" or dayOfWeek == "Tuesday" or dayOfWeek == "Wednesday" or dayOfWeek == "Thursday":
    favThings = input(f"Tell me what you usually do on {dayOfWeek}: ")
else:
    print("This is not a valid day, please try again")
if dayOfWeek == "Monday":
    if favThings == "going out" or favThings == "learning English" or favThings == "going to gym":
        print("Well,", name,",",dayOfWeek,"is usually the beginning and,",favThings,"is what you should be doing, carry on")
    else:
        print("I'm sure on",dayOfWeek,"you can do that, but I can't motivate you on this")
if dayOfWeek == "Tuesday":
    if favThings == "visting friends":
        print("Awesome!, you should",favThings,"on",dayOfWeek)


