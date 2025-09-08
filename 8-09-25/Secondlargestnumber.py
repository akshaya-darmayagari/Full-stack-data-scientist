def secondlar(l):
    l.sort()
    return l[-2]
l=list(map(int,input().split()))
print(secondlar(l))