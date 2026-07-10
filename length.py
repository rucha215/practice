def length(a):
    if len(a) < 8:
     print("weakpassword")
    elif 8<= len(a) <= 12:
     print("medium password")
    else:
     print("strong password")  
  
 
def main():
  a = input("enter a password")
  length(a)

if __name__ == "__main__":
    main()




