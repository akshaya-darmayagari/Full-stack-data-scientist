def prime(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c=c+1
    if c==2:
        print(a,"is a prime number")
    else:
        print(a,"is not a prime number")
n=int(input("Enter a number:"))
prime(n)