a=input()
b=input()
a=[ch for ch in a]
b=[ch for ch in b]
if(len(a)==len(b)):
    a.sort()
    b.sort()
    if(a==b):
        print("True")
    else:
        print("False")
else:
    print("False")