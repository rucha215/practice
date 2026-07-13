def challege():

    name = input("enter your name")
 
    
    total = 0
    for i in range(1,6):
        marks = int(input("enter marks:"))
        total = total + marks

    percentage = total / 5

    if percentage >= 90:
        print("A")
    elif percentage >= 80:
        print("B")
    elif percentage >= 70:
        print("c")
    elif percentage >= 60:
        print("D")
    else:
        print("Fail")
    
    return name, total ,percentage 

name, total, percentage = challege()

print("\n------ Student Result ------")
print("Name       :", name)
print("Total      :", total)
print("Percentage :", percentage)


    
    


    
    

                