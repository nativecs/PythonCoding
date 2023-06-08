languages = ["Hi Welcome to Pythin Multilangauge", "हाय पायथन मल्टी लैंग्वेज में आपका स्वागत है", "Привет, добро пожаловать в многоязычный Питон", "Hola, bienvenido a Python Multi Language"]

import random
import time
print("Welcome to random greeting generator")
time.sleep(0.4)
print()
print("Available Languages are:")
time.sleep(0.4)
print("\nEnglish \nHindi \nRussian \nSpanish")
select = input("Please select your greeting: ")

if select == "English":
    print(languages[0])
elif select == "Hindi":
    print(languages[1])
elif select == "Russian":
    print(languages[2])
elif select == "Hindi":
    print(languages[3])
else:
    print("Random Greeting")
    genLang = random.randint(0,3)
    print(languages[genLang])





