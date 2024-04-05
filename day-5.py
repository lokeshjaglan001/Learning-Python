# here we created a program in which any user can give the length and breadth of the rectangle and he or she will return the area of the rectangle and also the perimeter of it.
length = int(input("Enter the length of Rectangle :"))
bredth = int(input("Enter the breadth of the Rectangle :"))

Area = (length*bredth)
perimeter = 2*(length+bredth)

print("So the area of rectangle is" , Area ,"m²", "and the perimeter of rectangle is " , perimeter, "m")

#here we created a program in which user can give the radius of the circles and return the area and circumference of the circle.
radius = int(input("Enter the radius of the circle : "))
def area_peri(radius):
  print("So the area of the Circle is " , (22/7)*(radius**2)  , "m²")
  print("The Circumference of the Circle is" , 2*(22/7)*radius , "m")
area_peri(radius)

#here we created a program in which user will enter the circumference of the circle and return the area of the circle.
def area(Circumference):
  radius2 = Circumference/(2*3.14)  
  area = "So the area of the Circle is " , 3.14*(radius2**2) , "m²"
  print(area)

Circumference = int(input("Enter the Circumference of the circle : "))  
area(Circumference)

#here we created a program in which user will enter the size of side of Square and return the area of the square .
def square(side):
  area = "So the area of the Square is " , side**2 , "m²"
  print(area)
side = int(input("Enter the Size of Side of Square : ")) 
square(side)

#here we created a program in which user will enter the two numbers and then the program will automatically replace the values of both the variables .

n1 = int(input("Enter Your First No. : "))    
n2 = int(input("Enter Your second No. : "))  
Temp = n1
n1 = n2
n2 = Temp
print("Your first no. is : " , n1)
print("Your second no. is : " , n2)

# here we created a program in which user will enter 4 numbers and then the program will return the Biggest No.
n1 = int(input("Enter the first No. :"))
n2 = int(input("Enter the second No. :"))
n3 = int(input("Enter the third no. :"))
n4 = int(input("Enter the fourth No. :"))

if n1 < n2 :
    max1 = n2
else :
    max1 = n1
if n3 < n4 :
    max2 = n4
else :
    max2 = n3
    
if max1 < max2 :
    print("The Biggest No. is :" , max2) 
else :
    print("The Biggest No. is :" , max1)    
                   
# here we created a program in which the user will enter the two numbers and then the program will return the whole square (a+b)² value.
def whole_sq(No1 , No2):
   return ((No1)**2 + (No2)**2 + 2*No1*No2)
No1 = int(input("Enter first number : "))
No2 = int(input("Enter second number : "))   
sq= whole_sq(No1 , No2)
print("The whole square of both numbers is " , sq )

#here we created a program in which the user will provide the both diameter of the rhombus and the function will return the area of rhombus.
d1 = int(input("Enter the first digonal :"))
d2 = int(input("Enter the second digonal :"))

area = (1/2)*d1*d2
print("So the area of rhombus is " , area , "m²")