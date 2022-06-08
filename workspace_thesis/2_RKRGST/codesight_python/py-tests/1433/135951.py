k,l=map(int,input().split())
c=0
if k == 1:
    k=k+1
for j in range(k,l+1,1):
    i=2
    sw=True
    while i*i<=j:
        if j%i==0:
            sw=False
           
        i=i+1
    if sw:
        c=c+1
print(c)
