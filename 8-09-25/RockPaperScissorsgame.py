import random
u="Rock"
print("User: ",u)
c=random.choice(["Rock","Paper","Scissors"])
print("Computer(random): ",c)
if u==c:
    print("It's a Tie")
elif (u=="Rock" and c=="Scissors") or (u=="Paper" and c=="Rock") or (u=="Scissors" and c=="Paper"):
    print("You chose",u,"and computer chose",c)
    print("You Win!")
else:
    print("You chose",u,"and computer chose",c)
    print("Computer Wins!")