from math import sqrt
a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
d=b*b-4*a*c
s1=(-b+sqrt(d))/(2*a)
s2=(-b-sqrt(d))/(2*a)
print("Roots are: ",s1,s2)