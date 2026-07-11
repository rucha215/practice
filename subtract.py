def subtract(a , b):
    c = a - b
    return c

def main():
    a = int(input("enter a number :"))
    b = int(input("enter a number:"))
    result = subtract(a,b)
    print("subraction is:", result)

if __name__ == "__main__":
    main()