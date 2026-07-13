def reversetable(num):
    for i in range(10, 0 ,-1):
        print(num , "x" , i, "=" , num*i )

num = int(input("enter a number:"))
print(reversetable(num))