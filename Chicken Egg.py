# Input statements
chicken_name = input("Enter the name of the chicken: ")
egg_count = int(input("Enter the number of eggs the chicken lays per day: "))
days = int(input("Enter the number of days passed: "))
farmer_name = input("Enter the name of the farmer: ")

# Story
print("\nOnce upon a time, there was a chicken named", chicken_name + ".")
print(chicken_name, "laid", egg_count, "eggs every day.")

total_eggs = egg_count * days
print("After", days, "days,", chicken_name, "had laid a total of", total_eggs, "eggs.")

if total_eggs > 0:
    print("The farmer,", farmer_name + ", was happy to collect the eggs.")

    if total_eggs > 10:
        print("He sold some eggs in the market and earned a good profit.")
    if total_eggs <= 10:
        print("He kept the eggs for his family's breakfast.")

    # Modulo and Division calculations
    dozens = total_eggs // 12
    leftover_eggs = total_eggs % 12

    if dozens > 0:
        if leftover_eggs > 0:
            print("The farmer packed", dozens, "dozen eggs and", leftover_eggs, "extra eggs.")
        if leftover_eggs == 0:
            print("The farmer packed", dozens, "dozen eggs.")
    if dozens == 0:
        print("The farmer packed", leftover_eggs, "eggs.")
if total_eggs <= 0:
    print("Unfortunately, there were no eggs to collect.")

print("\nThe end.")
