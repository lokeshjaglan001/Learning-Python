# Here are 8 test function questions for you:

# 1. Simple Function: Write a function that takes a string and returns the number of vowels in the string.
# 2. Function with Multiple Parameters: Write a function that takes three arguments: the principal amount, rate of interest, and time (in years). It should return the simple interest calculated using the formula \(SI = \frac{P \times R \times T}{100}\).
# 3. Function with Default Arguments: Write a function to calculate the area of a rectangle. The function should have default values for length and width as 1.
# 4. Function with Variable-Length Arguments: Write a function that accepts any number of string arguments and returns the longest string.
# 5. Lambda Function: Write a lambda function that takes two numbers and returns their greatest common divisor (GCD).
# 6. Higher-Order Function: Write a function that takes another function and a list as arguments and returns a list of results after applying the function to each element in the list.
# 7. Nested Functions: Write a function `outer` that contains a nested function `inner`. The `inner` function should multiply its argument by 5, and the `outer` function should return the result of calling `inner` with a given argument.
# 8. Recursion Function: Write a recursive function to compute the nth Fibonacci number.

### Program ###
1. def main(string):
    vowels = "aeiouAEIOU"
    result = []
    for char in string:
        if char in vowels:
            result.append(char)
    return result
	
Para = "Hello this my sample paragraph and this paragraph is used for my program"
print(main(Para))

2. principle = int(input("Enter the Principle Amount : "))
interest = int(input("Enter the Rate of Interest : "))
years = int(input("Enter the Interest Time(Years) : "))
def main(principle , interest , years):
	
	simple_interest = (principle*interest*years)/100
	
	amount = principle + simple_interest
	return amount
print("The Total amount after the Interest will be :",main(principle , interest , years))

3. length = int(input("Enter the Length of Rectangle : "))
width = int(input("Enter the Width of Reactangle : "))

def Rectangle_area(length=1 , width=1):
	   area = (length*width)
	   return area
print("The Area of Rectangle will be :",Rectangle_area(length,width))

4. number = int(input("How many String you want to enter : "))
List = []
for i in range(number):
	Strings = input("Enter the String : ")
	List.append(Strings)
Sorted = (sorted(List))
print(Sorted)
print(Sorted[0])

5. def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm

num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
	
result = (num1*num2)/(lcm(num1,num2))

print(result)

6. list = ["a","b","c","d","e","f","g","h","i","j","k"]
new_list = []
def main(func,data_list):
    for char in data_list:
    	result = func(char)
    	#result = bin(ord(list))
    	new_list.append(result)
    print(new_list)
    
def binary(char):
	return bin(ord(char))
main(binary , list)

7. num = 5
def outer(num):
	def inner():
		print(num*5)
	inner()
outer(num)

8. num = 6
def fibonaci(num):
	if num == 0 :
		return 0
	elif num == 1 :
		return 1
	else :
		return fibonaci(num-1) + fibonaci(num-2)
print(fibonaci(num))
