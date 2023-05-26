import time
def newPrint(colour, word):
  if colour== "red":
    print("\033[31m", word, sep="", end="")
  elif colour == "green":
    print("\033[0;32m", word, sep="", end="")
  else:
    print("\033[0m", word, sep="", end="")


print("Super Subroutine")
print("With my ", end="")
newPrint("red", "new program")
newPrint("reset", " I can just call red('and') ")
newPrint("green", "it will print in red ")

