def correctpassword():
    password = "acbdf"
    enteredpass = input("enter password")

    while enteredpass != password:
        enteredpass= input("wrong try again")
    print("success you are logged in ")  

result = correctpassword()  
print(correctpassword())  