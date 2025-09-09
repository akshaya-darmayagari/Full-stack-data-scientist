a=input("Enter a string:")
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print("Charcters and their frequencies in given string are:",d)
