# Question 1 (full GCSE style) A theme park ride allows entry if: height ≥ 120 cm AND age ≥ 10 OR the person is with an adult

age = int(input("Enter your age: "))
height = int(input("Enter your height in cm: "))
adult = input("Are you accompanied by an adult? yes/no: ")

def check(age, height, adult):
    if (height >= 120 and age >= 10) or adult == "yes":
        print("You are allowed entry")
    else:
        print("Not allowed")

check(age, height, adult)

        

