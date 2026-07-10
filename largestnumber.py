def largestnumber(n1 , n2 ,n3):
    if (n1 >= n2 and n1 >= n3):
        print("largest number is " , n1)
    elif (n2 >= n1 and n2 >= n3):
        print("largest number is " , n2) 
    else:
        print("largest number is " , n3)

def main():
    n1 = int(input("num1"))
    n2 = int(input("num2"))
    n3 = int(input("num3"))
    largestnumber(n1 , n2 , n3)

if __name__ == "__main__":
    main()





