# Here we learn about while loop
i = 0 
while i < 50 :
    print(i)  
    i = i + 1
    
# Here we saw how to print list    
list = [5,6,6,5,9,8,7,1,2,12,87,458,846,65,65,655]
for item in list:
    print(item)     

# here we learn how we can print a fix no. of elements from any arry
for i in range(0,7):
    print(i)  
 
# here we learn how to print any string after the loop finished    
for item2 in list:
    print(item2)  
else:
    print ("Done")  

# here we learn about the break statement in which we can stop any loop when any give element print
for a in range (0,800):
    print(a) 
    if a == 115:
        break