def calculator( num1 , num2 , operator):
    match operator:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2


def main():
    num1 = int(input("enter a number:"))
    num2 = int(input("enter a number:"))
    operator = input("enter an operator")

    result=calculator(num1 , num2 , operator)
    print("output", result)

if __name__ == "__main__":
    main()
