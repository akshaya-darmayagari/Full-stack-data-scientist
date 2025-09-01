s=input("Enter a number: ")
l=len(s)
a=int(s)
b=a
su=0
while(a>0):
    r=a%10
    su+=r**l
    a=a//10
if b==su:
    print("Yes,it is an armstrong number")
else:
    print("No it's not an armstrong number")
