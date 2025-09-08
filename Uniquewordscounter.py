import collections
def unique(l):
    d=collections.Counter(l)
    return d
l=list(map(str,input().split()))
d=unique(l)
print(d)