# First Type of Function : Simple Function
Name = input("Enter Your Name : ")

def main(Name):
	
	return f"Hello , {Name}"
	
print(main(Name))
	
# Second Type of Function : Function with Multiple Parameters
First = int(input("Enter First Number : "))

Second = int(input("Enter Second Number : "))

def addition(First , Second):
	
	return First + Second
	
print("The addition will be" , addition(First,Second))

# Third Type of Function : Function with Default Arguments
def greet(name="Humanshu"):
	
	return f"Hello {name}"
	
# Here the function will use the default value
print(greet())

# Here the function will use the given value
print(greet("Jaat"))

# Fourth Type of Function : Function with Variable-Length Arguments
# A) args(for non-keyword arguments)
def addition(*args):
	
	return sum(args)
	
print(addition(1,2,4,3,2,4,4,3))

# B) kwargs(for keyword arguments)
def print_info(**kwargs):
	
	for key,value in kwargs.items():
		
		print(f"{key} : {value}")
		
print_info(Name="Humanshu",Age=18,Village="Brahman Majra")

# By using *args and **kwargs, you can create functions that are more dynamic, flexible, and capable of handling a wide range of input scenarios. This can be particularly useful in situations where the input data is not fixed or predictable.

# Fifth Type of Function : Lambda Function
num = int(input("Enter the number whose Square you want : "))

Square = lambda num : num**2

print(f"The Square of {num} is",Square(num))

# Sixth Type of Function : Higher-Order Function
# A) Passing function as arguments
def higher(func , value):
	
	return func(value)
	
result = higher(lambda x : x**2 , 5)

print(result)

# B) Returning Function
one = int(input("Enter the number on which you want the power : "))

two = int(input(f"Enter the power you want on {one} : "))

def first(n):
	
	return lambda x : x**n
	
result2 = first(two)

print(result2(one))

# Seventh Type of Function : Nested Functions :- Functions defined within other Function
def outer_function(num):
    def inner_function():
        return num**num
    
    return inner_function()

print(outer_function(4))

# Eighth Type of Function : Recursion Functions :- Function that calls itself
def factorial(n):
	if n == 1 :
		return 1
	else :
		return n * factorial(n-1)
print(factorial(4))

# Ninth Type of Function : Generators Functions :- Functions that yield values one at a time using the yield keyword. They are used to generate a sequence of values.
def countdown(n):
	while n > 0 :
		yield n
		n -= 1
for i in countdown(7):
        print(i)

# Tenth Type of Function : Decorators :- Functions that take another function and extend or modify its behavior.

def first(text):
	def second():
		print("hello this is my first paragraph")
		text()
		print("hell this is my second paragraph")
	return second
		
@first
def hello():
	print("Hello bhai ab yo second paragraph suru hoga ! ")
hello()

# Eleventh Type of Function : Function Annotations :- Python allows you to add type hints to functions

a = int(input("First number : "))
b = int(input("Second number : "))

def add(a:int , b:int)-> int :
	return a + b
print(add(a,b))