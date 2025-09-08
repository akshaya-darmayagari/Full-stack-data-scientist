a=input()
a.lower()
v,c=0,0
for i in a:
    if i in "aeiou":
        v+=1
    else:
        c+=1
print("Vowels:",v,"Consonants:",c)