alvaro=[ "A", "B", "C"]
edwin=["B", "A", "B", "C"]
gabriel=["C", "C", "A", "A", "B", "B"]
s=0
p=0
q=0
c=int(input())
a=input()
for i in range(c):
    if alvaro[i%len(alvaro)]==a[i]:
        s+=1
    if edwin[i%len(edwin)]==a[i]:
        p+=1
    if gabriel[i%len(gabriel)]==a[i]:
        q+=1
sm=[s,p,q]
m=max(s,p,q)
prom=[]
if m==sm[0]:
    prom.append("Alvaro")
if m==sm[1]:
    prom.append("Edwin")
if m==sm[2]:
    prom.append("Gabriel")
print(m)
for k in range(len(prom)):
    print(prom[k])