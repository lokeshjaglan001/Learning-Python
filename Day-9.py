name = input("What's your name : ")
print(f"Hello {name}!")

color = input("Pick one color:\n1 - Red\n2 - Yellow\n3 - Green\n")

if color == "1":
    print("Calm down, you are likely to be angry!")
elif color == "2":
    print("Keep doing your work, you are likely to be bored!")
elif color == "3":
    print("Yeah boy, you are likely to be happy!")
    input("What's the good news tell us also : ")
    print("Congratulations ! Boyyyy 🥳 🎊")
else:
    print("Something went wrong. Please try again!")



for i in range(1,17):
    print("Hello Bro !")

gender = input("What's your gender:\n1 - Male\n2 - Female\n3 - Prefer not to say\n")

if gender == "1":
    print("Ok, you are male!")
    
elif gender == "2":
    print("Ok, you are female!")
    
elif gender == "3":
    while True:
        var1 = input("Tell us:\n No\n")
        if var1.lower() == "no":
            print("Why Nooooo!")
        else:
            print("Something went wrong!")
            break  # Exit the loop if input is not "No" or "no"
else:
    print("Invalid input, please enter 1, 2, or 3!")