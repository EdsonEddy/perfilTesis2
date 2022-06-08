cas=int(input())
l=[]
while cas>0:
    x=input()
    r=x[::-1]
    l.append(r)
    cas-=1
l=l[::-1]
for i in range(len(l)):
    print(l[i])