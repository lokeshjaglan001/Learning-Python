list = [1,2,3,4,5,6,4,78,58479,4,5,4,5,6,4,5,8,77,55,8,4,56,412,455,22,4226]
list.sort()
print(list)

print(len(list)) 

list.remove(5)
print(list)
# dictionary system
dict = {
    "Name" : "Lokesh",
    "Age" : [16],
    "Country" : ["India"],
    "Class" : "11th"
}
print(dict.items())
# updating system in the dictionary
dict.update({"Country": "Bharat"})
print(dict)

# dictionary use by input
dictionary = {
    "eating" : "Khana",
    "bathing" : "Nahana",
    "reading" : "Padhna"
}

print(dictionary.keys())
input_user = input("Which word's meaning do you want :").lower()
print(dictionary[input_user] )

# Here we can count any element in our list which is given through input
list = [7,0,8,0,0,9]
print(list)
count_list = list.count(int(input("Which integer do you want to Find : ")))
print(count_list)

# Here we can add any element in our List which is given by us
list2 = [5,6,4,2,6,3,4,8,9,4,2,5]
list2.append(54)
print(list2)

# Here we can add any element in our list on any index No.
list3 = [5,6,4,2,6,3,4,8,9,4,2,5]
list3.insert(7,51)
print(list3)

# Here we saw how Logical operators works
a = 9
b = 6
# Here we get false because our second condition is wrong and when and operator is used both conditions have to be true to give true in our output
print(a>b and a<b)

# Here we get true because in 'OR' Logical operator one condition out of both must be true to give true in our output
print(a>b or a<b)

# Here we get true because 'NOT' Logical operator always opposite the output and here the condition should give false but because of not operator it will give true output
print(not a<b)

# Question:- Create an empty dictionary. Allow your 4 friends to enter their favourite language as values an uses key as their names.Assume that the names are unique.
dict2 = {
}
for i in range(0,4):
 input_frnd = input("What is your name : ")
 frnd_lang = input("Which is your favourite Language : ")
 dict2.update({ input_frnd  :  frnd_lang})
print(dict2)

#Relational operators
a = 10 
b = 16
# Here A is not equal to the B so this condition is wrong then it will go to the elif
if (a == b) :
    print("Yes these are equal")
# Here A is neither greater not equal to the B so it will also go to the next elif condition    
elif (a >= b) :
    print("Yes A is bigger")
# Here B is greater than A so this statement will run and print the following statement  
elif (a <= b) :
    print("Yes B is bigger")    
# It always run when no condition left in the code   
else :
  print("Something wents wrong")

usersinp = []
for i in range(0, 4):
    usersinp.append(int(input("Enter Number : ")))
usersinp.sort()
print(usersinp[-1], "is the biggest number")



# Name length detect whether it is less than 10 or more than 10 characters
username = input("Enter your Name here :")
usercount = len(username)
if usercount >= 10:
    print("Your username length is more than or equal to 10 characters")
else:
    print("Your username length is less than 10 characters")