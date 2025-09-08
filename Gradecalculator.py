def gradecal(l):
    m=sum(l)/len(l)
    if(m>=90):
        return 'A'
    elif(m>=80):
        return 'B'
    elif(m>=70):
        return 'C'
    elif(m>=60):
        return 'D'
    else:
        return 'Fail'
l=list(map(int,input().split()))
print(gradecal(l))