#Program to check whether the user is child, teenager, adult or senior
for i in range(1,5) :
	age = int(input("Enter Your Age : "))
	if age < 13 :
		print("You are a Child ! ")
	elif 13 < age < 19 :
		print("You are a Teenager !")
	elif 19 < age < 30 :
		print("You are an Adult Boy !")
	elif 30 < age :
		print("You are a Senior Boy !")
	else :
		print("Something wents Wrong !")

#Program to check whether the number is positive or negative or zero
for i in range(1,5):
	num = int(input("Enter any Number : "))
	if num > 0 :
		print(f"The {num} is Positive !")
	elif num == 0 :
		print("This is Zero")
	elif num < 0 :
		print(f"The {num} is Negative !")
	else :
		print("Something wents Wrong !")

#Program to check the year is Leap or not 
category = int(input(" What do you want to check :\n Year -- 1\n Sanctuary -- 2\n >>> "))
for i in range(1,5):
	if category == 1 :
		year = int(input("Enter the Year : "))
		if year % 4 == 0 :
			print(f"The {year} is a Leap Year !")
		elif year % 4 != 0:
			print(f"The {year} ia not a leap year !")
		else :
			print("Something wents Wrong !")
	elif category == 2 :
		sanctuary = int(input("Enter that Sanctuary : "))
		if sanctuary % 400 == 0 :
			print(f"The {sanctuary} is a Leap Year !")
		elif sanctuary % 400 != 0:
			print(f"The {sanctuary} ia not a leap year !")
		else :
			print("Something wents Wrong ! ")
	else :
		print("Something wents Wrong !")