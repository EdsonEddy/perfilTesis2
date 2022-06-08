a,b=map(int,input().split())
p=a
c=1
while(p>=10):
    p=p/10
    c+=1
s=int(str(a)[b-1])
print(c,s)