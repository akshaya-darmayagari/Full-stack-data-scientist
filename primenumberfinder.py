n=int(input())
l=[]
for i in range(2,n):
    c=0
    for j in range(2,i):
        if i%j==0:
            c+=1
    if c==0:
        l.append(i)  
print(l)