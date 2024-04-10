#here we created a program in which user will enter the natural number and the program will print the sum of natural numbers.

N = int(input("Enter the no. to ehich you want addition :"))
sum =0
for i in range(1,N+1):
  sum = sum + i
print("The sum of first",N,"natural no. is",sum)

#here we creative a program in which program will return the greeting name started with s character
l1 = ["Harry","Soham","Sachin","Rahul"]
for name in l1:
  if name.startswith("s"):
    print("Hello",name)

#here we created a program in which user will enter their number of subjects and then enter the subject name and its marks and then the program will return the dictionary of it
n = int(input("How many subjects do you have : "))
dic = {}
for i in range (0, n ):
    Sub = input("Which Subject : ")
    Marks = int(input("Enter your Marks : "))
    dic.update({ Sub : Marks })
print(dic)