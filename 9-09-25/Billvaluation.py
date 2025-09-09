try:
    n=int(input("Enter number of units:"))
    bill=0
    if n<100:
        bill+=n*5
    elif n>100 and n<201:
        bill+=100*5+(n-100)*7
    else:
        bill+=100*5+100*7+(n-200)*10
    print("Total bill:",bill)
except:
    print("Invalid input(no. of units must be an integer)")
finally:
    print("Bill processing completed")