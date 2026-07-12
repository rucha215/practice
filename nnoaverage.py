def average_of_numbers():
    n = int(input("Enter how many numbers you want to input: "))

    total = 0
    i = 1

    while i <= n:
        num = int(input("Enter number: ",i))
        total = total + num
        i = i + 1

    average = total / n
    return average

result = average_of_numbers()
print("Average =", result)


