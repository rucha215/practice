def oddeven(number):
    if (number % 2 == 0 ):
        print("even")
    else:
        print("odd")
        
    
def main(): 
    a = int(input("enter a number:"))
    oddeven(a)

if __name__ == "__main__":
    main()