n=int(input("Enter balance amount: "))
a=int(input("Enter withdrawl ammount:"))
try:
    if a>n:
        raise Exception("Withdrawl amount is grater than balance")
except:
    print("Withdrawl amount is grater than balance")
