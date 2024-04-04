#Here we created a program in which user enter there marks and then he will get the grade.
Marks = int(input("Enter your marks: "))
if Marks >= 90:
  print ("Excellent")
elif Marks >= 80:
  print ("Grade A")
elif Marks >= 70:
  print ("Grade B")
elif Marks >= 60:
  print ("Grade C")
elif Marks >= 50:
  print ("Grade D")
else :
  print ("Grade E")
#here we created a program in which a user can enter any word which user want to find whether it is available in the paragraph or not
Para = "The dog's owner is harry  " \
                   "my brother is also a good programmer and i recently"
print(Para)
user = input("Enter the word which you want to find in the paragraph: ")
if Para.find(user) == -1:
  print("No", user , " not found in the paragraph")
else:
  print("Yes", user  , "found in the paragraph")

#here we learn how to create a simple function in python and how to execute it
name = input("Enter your name here : ")
def greet(name):
  greeting = "Hello " + name 
  print(greeting)
greet(name)