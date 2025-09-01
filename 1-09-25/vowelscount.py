a=input("Enter a string : ")
v=0
c=0
for i in a:
    if(i=='a'or i=='e'or i=='o'or i=='i'or i=='u'or i=='A'or i=='E'or i=='O'or i=='U'or i=='I'):
        v+=1
    else:
        c+=1
print("Vowels: ",v,"\nConsonants: ",c)