#here we created a program in which user will enter the value and the program will return the full multiplication table of that no.
inp = int(input("Enter the number whose table you want :"))
for i in range(1 , 11):
    mul = inp*i
    print(mul)

#here we created a program in which the user will enter the number and the program will return if the number is prime or composite
no = int(input("Enter the no which you want to check whether it is prime or not :"))    
for i in range(2, no):
    if no % i == 0:
        print("Your No. is composite")
        break
else:
    print("Your No. is Prime")

#here we created a program in which the user will enter the number and the program will return the factorial of that number
f = int(input("Enter the no. whose factorial you want:"))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(f)
print(f'The factorial of {f} is: {result}')