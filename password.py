def password(n):
    if n == "python1234":
        return("acces granted")
    else:
        return("access denied ")

n = input("enter your password")
result = password(n)
print(result)