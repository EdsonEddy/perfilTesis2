n=int(input())
a=input().split()
c=[]
for i in range(len(a)-1,-1,-1):
	c.append(a[i])
if c==a:
    print("SI")
else:
    print("NO")