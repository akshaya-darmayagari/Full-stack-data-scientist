a=input("Select operation(+,-,*,/):")
b=int(input("Enter first number:"))
c=int(input("Enter second number:"))
if a=='+':
    print(b+c)
elif a=='-':
    print(b-c)
elif a=='*':
    print(b*c)
elif a=='/':
    if c>0:
        print(b/c)
    else:
        print("Denominator cannot be zero")
