import os, time
DailyDiary = []
print("**** Welcome to Joshua's Daily Scheduler ****")
print()


def dailyroutine():
    print()
    for schedule in DailyDiary:
        print(schedule)
    print()
while True:
    menu = input("view, add or edit: ")
    if menu == "add":
        schedule = input("What is on the agenda?: ")
        DailyDiary.append(schedule)
    elif menu == "edit":
        schedule = input("Which agenda you would like to edit?: ")
        DailyDiary.remove(schedule)
    elif menu == "view":
        print("******** Your Agenda so far ********")
        print()
        dailyroutine()
    dailyroutine()