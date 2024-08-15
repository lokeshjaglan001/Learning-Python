#I created a program in which the code will generate a random number between 0 to 100 and then the user have to predict what should be the number.

import random

random_number = random.randrange(1,100)

guess = int(input("What you think the number is : "))

if guess == random_number :
    print("congratulations 🎉 , You found the number !")
else:
    while not guess == random_number :
      guess =  int(input("Try again to find number : "))
    print("congratulations 🎉 , You found the number !")

#I created a program in which firstly user give input that how many number the user want to check and then the user enter the number to check whether the number is Even or Odd.

Times = int(input("How many numbers do you want to check whether they are Even or Odd: "))

for i in range(Times):
    Number = int(input("Enter the number to check whether it is Even or Odd: "))
    if Number % 2 == 0:
        print(f"The number {Number} is Even")
    else:
        print(f"The number {Number} is Odd")