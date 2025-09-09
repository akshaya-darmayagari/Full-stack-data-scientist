def bill():
    n=int(input("Enter number of units:"))
    bill=0
    if n<100:
        bill+=n*5
        return bill
    elif n>100 and n<201:
        bill+=100*5+(n-100)*7
        return bill
    elif n>200:
        bill+=100*5+100*7+(n-200)*10
        return bill
print("Total bill:",bill())