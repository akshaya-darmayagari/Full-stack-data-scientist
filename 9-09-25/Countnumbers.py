a=list(map(int,input().split(" ")))
p,n,z=0,0,0
for i in a:
    if i>0:
        p+=1
    elif i<0:
        n+=1
    else:
        z+=1
print("Positive:",p)
print("Negative:",n)
print("Zeroes:",z)