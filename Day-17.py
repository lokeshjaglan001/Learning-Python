#Program to check whether the word is Palindrome or not
string = input(" Enter the word : ")
temp = reversed(string)
if temp == string :
	print(f" {string} is Palindrome !")
else :
	print(f" {string} is not palindrome !")

#Program to print the Fibonacci series to the nth term
num = int(input("Enter the Number :"))
def fibonaci(n):
	if n <= 0 :
		return 0
	elif n == 1 :
		return 1
	else :
		return fibonaci(n-1) + fibonaci(n-2)
for i in range(1,num+1):
	print(fibonaci(i))