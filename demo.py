i = 0
a = 0
c = 0
while i!= 2:
    height = int(input("what is your height: "))
    question = input("are you an adult? ")
    if question == "yes" or "Yes":
        a = a +1
    if question == "no":
        if height < 140:
            print("you need support")
            c  = c+ 1
        else:
            print("you can go alone")
            a = a + 1
    i = i + 1




