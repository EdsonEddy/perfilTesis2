a,b=map(int,input().split())
p=0
if(a==1):
   a=a*2
for n in range(a,b+1):
   i=2
   sw=True
   while(i*i<=n):
     if n%i==0:
       sw=False
       break
     i=i+1
   if sw:
     p=p+1
print(p)