c=0
cp=0
a,n=map(int,input().split())
for j in range(a,n+1):
      for i in range(1,j+1):
        if j%i==0:
            c=c+1
      if c==2:
        cp=cp+1
      c=0    
print(cp)