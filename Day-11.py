#Password Generator
import random
import string

times = int(input("How many passwords do you want? "))

for i in range(times):
    length = int(input("How many characters do you want in your password? "))
    
    if length > 0:
        character_pool = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choices(character_pool, k=length))
        print(password)
    else: 
        print("Please enter a positive number")