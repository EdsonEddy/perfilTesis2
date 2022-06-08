a,b=map(int,input().split())
l=a
e=1
while(l>=10):
   l=l/10
   e+=1
s=int(str(a)[b-1])
print(e,s)