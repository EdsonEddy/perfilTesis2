import math
t=input()
a=input()

busq=t.find(a)
p=busq
while busq!=-1:
    print(p)
    t=t[busq+1:]
    busq = t.find(a)
    p=p+busq+1
