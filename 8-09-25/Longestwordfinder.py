a=input()
l=a.split(" ")
le=0
w=""
for i in l:
    if len(i)>le:
        le=len(i)
        w=i
print(w)