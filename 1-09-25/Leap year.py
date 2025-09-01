a=int(input("Enter a year:"))
if((a%4==0 and a%100==0)or a%4!=0):
    print("It is not a leap year")
elif(a%4==0 or a%400==0):
    print("It is a leap year")