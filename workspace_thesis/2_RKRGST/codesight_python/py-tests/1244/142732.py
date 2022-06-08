from math import*
n=int(input())
for i in range(n):
    c=input().split()
    li=[]
    for h in c:
        li.append(h)
    if li[0]=="circle":
        a=pi*float(li[1])**2
    else:
        a=float(li[1])*float(li[2])
    print("{0:.2f}".format(a))