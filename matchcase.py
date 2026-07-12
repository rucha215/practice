def week(num):
    match num:
        case 1:
            return("monday")
        case 2:
            return("tuesday")
        case 3:
            return("wednesday")
        case 4:
            return("friday")
        case 5:
            return("sunday")

num = int(input("enter a number between 1-5:"))
print(week(num))         
    
