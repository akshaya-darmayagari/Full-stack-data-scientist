def fib(n):
    a,b=0,1
    l=[]
    if(n==0):
        l.append(a)
    elif(n==1):
        l.append()
    else:
        for i in range(0,n):
            l.append(a)
            a,b=b,a+b
    return l
n=int(input("n= "))
print(fib(n))
    