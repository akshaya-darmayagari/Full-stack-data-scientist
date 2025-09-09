n=int(input("Enter number of students:"))
d={}
for i in range(n):
    name=input()
    att=int(input())
    d[name]=att
print("Students with attendance less than 75% are:")
for i in d:
    if d[i]<75:
        print(i,end=" ")