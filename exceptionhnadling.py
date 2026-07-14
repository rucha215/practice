a = int(input("enter the first number"))
b = int(input("enter the second number"))
try:
    div=a/b
    print("result is", div)
except ZeroDivisionError:
    print("error the second number cannot be zero for divsion")







