n=input()
s,d,x=0,"",len(n)
for i in range(x):
     if n[i]=="1":
        s+=1
     else:
        d+=str(s)
        s=0
d=d+str(s)
print(d)