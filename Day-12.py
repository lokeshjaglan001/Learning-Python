#Word counter and Character counter 

Name = "Clear writing is key. Be concise, relevant, and ensure each word adds value to the message."

name = list(map(len, Name.split()))

nameno = sum(name)

print(f"Each word's length is {name}")

print(f"Total Number of Characters in this paragraph excluding spaces is {nameno}")

#Multiplication table generator

number = int(input("Enter the integer whose Yable do you want : "))
for i in range(1,11):
    print(f"{number}X{i}= {number*i}")
