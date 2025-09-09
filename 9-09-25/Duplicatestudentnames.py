a=list(map(str,input("Enter student names: ").split(",")))
print("Duplicate student names are:")
for i in a:
    if a.count(i)>1:
        print(i,end=" ")
        a.remove(i)