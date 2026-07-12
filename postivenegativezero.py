def number(n):
    if n > 0:
        return("postive")
    elif n < 0:
        return("negative")
    else:
        return("zero")

n = int(input("enter a number"))              
print(number(n))