year = int(input("Which year do you want to check? "))

x=year%4
y=year%100
z=year%400
if x==0:
    if y==0:
        if z==0:
            print("Leap year")
        else:
            print("Not leap year")  
    else:          
        print("Leap year") 
else:
    print("Not leap year")    
