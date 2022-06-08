n=input()
s=0
d=""
x=len(n)
for i in range(x):
     if n[i]=="1":
        s=s+1
     else:
        d=d+str(s)
        s=0
d=d+str(s)

print(d)