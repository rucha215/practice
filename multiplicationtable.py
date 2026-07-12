def table(num):
    for i in range(1, 11):
        print( num, "x" , i, "=" , num*(i) )

num = int(input("enter a number"))
table(num)