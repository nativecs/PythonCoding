import random
print("Guess the Number, you have 3 tries")
number = random.randint(1,10)
count = 0
while count < 3:
  askUser = int(input("Enter your best guess: "))
  if askUser < number:
    count += 1
    print("your guess is too low, try again: count(s)",        count)
  elif askUser > number:
    print("your guess is too high, try again: count(s)",       count)
    count += 1
  elif askUser == number:
    print("brilliant, you have the right number")
    count += 1
    exit()
