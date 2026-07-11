def add(a , b):
     c = a + b
     return c 

def main():
    a = int(input("enter a number:"))
    b = int(input("enter a number: "))

    result = add(a,b)
    print("addintion is:", result)


if __name__ == "__main__":
    main()

