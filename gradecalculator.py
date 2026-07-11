def calculator(marks):
        #abx = ""
        if 90 <= marks <= 100:
           return "A"
           
        elif 80 <= marks <=89:
            return "B"
        else:
            return "C"

        #return abx
marks = int(input("enter marks:"))
result= calculator(marks)
print("grade =", result)


#def main purpose is to inport file