name = "harry"  # strings are immutable 

a = len(name)
print(a)

#len is used to calculate length

text = "hello world"
print(text.upper())  # Output: "HELLO WORLD" make ituppercase
print(text.lower())  # Output: "hello world" lowercase
print(text.title())  # Output: "Hello World"
print(text.capitalize())  # Output: "Hello world"

# syntax print(name.what you want())

text = "  hello world  "
print(text.strip())  # Output: "hello world"
print(text.lstrip()) # Output: "hello world  "
print(text.rstrip()) # Output: "  hello world"

# r is to remove whitespace from r
# l is to remove whitespace from l

text = "python is fun and is fun "
print(text.find("is"))
print(text.replace("fun", "awesome"))

# find is used only find 1 place 
# replace to replace everything 

text = "apple,banana,orange"
fruits = text.split(",")
print(fruits)  # Output: ['apple', 'banana', 'orange']

new_text = " - ".join(fruits)
print(new_text)  # Output: "apple - banana - orange"



text = "Python123"
print(text.isalpha())  # Output: False to tell all are alphabhet or not 
print(text.isdigit())  # Output: False is it a digit or not
print(text.isalnum())  # Output: True alphabet and number both 
print(text.isspace())  # Output: False is there any whitespace


print(ord('A'))  # Output: 65 
print(chr(65))   # Output: 'A'

# ord is to the number
# to know the alpha