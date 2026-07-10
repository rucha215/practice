def ticketprice(age , name):
    if  ( age < 5):
     print("Hello" , name, "\n Your Ticket is free")
    elif (5 <= age <= 17 ):
     print("Hello" , name, "\n Your Ticket is 150")
    elif (18 <= age <= 59):
     print("Hello" , name, "\n Your Ticket is 250")
    else:
     print("Hello" , name, "\n Your Ticket is 100")    

def main():
   age = int(input("enter a number:"))
   name = input("enter a name:")
   ticketprice(age , name)

if __name__ == "__main__":
    main()  
