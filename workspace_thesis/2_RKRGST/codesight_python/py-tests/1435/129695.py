a,b=map(int,input().split())
c=1
t=a
while(t>=10):
    t=t/10
    c+=1
s=int(str(a)[b-1])
print(c,s)