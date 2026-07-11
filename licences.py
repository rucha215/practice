def licence(age):
    if age >= 18:
        print("can have a licence")
    else:
        print("can't have a licence")

def main():
    age = int(input("enter your age:"))
    licence(age)

if __name__ == "__main__":
    main()