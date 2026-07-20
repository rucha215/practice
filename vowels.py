a = "coding is the best practice to make"
sum = 0
vowels = ['a', 'e', 'i ','o' ,'u']
for char in a:
    print(char)
    if(char in vowels):
        sum = sum + 1 

print(f"there are {sum} vowels in this sentence ")
