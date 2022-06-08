u=int(input())
x=input()
s=x.split(" ")
z=[]
for i in range(u):
    s[i]=int(s[i])
for i in range(u):
    if i==0:
        z.append(s[0])
    else:
        t=s[i]-s[i-1]
        z.append(t)
for i in range(u):
    z[i]=str(z[i])
n1=" ".join(z)
print(n1)