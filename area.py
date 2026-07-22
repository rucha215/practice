def calculate_area(length , width=10):
    area = length*width

    return area 
length = int(input("enter your length"))
width = int(input("enter your width"))
print(calculate_area(length , width))