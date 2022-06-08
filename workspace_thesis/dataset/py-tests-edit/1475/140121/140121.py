a,b,c=map(int,input().split())
s=input()
n=s.split(" ")
l=n[b:c+1]
y=reversed(l)
z=[]
for i in y:
    z.append(i)
n[b:c+1]=z[0:c+1]
for i in range(a):
    print(n[i])
