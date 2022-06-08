a=[ "A", "B", "C"]
b=["B", "A", "B", "C"]
c=["C", "C", "A", "A", "B", "B"]
c1=0
c2=0
c3=0
d=int(input())
p=input()
for i in range(d):
    if a[i%len(a)]==p[i]:
        c1+=1
    if b[i%len(b)]==p[i]:
        c2+=1
    if c[i%len(c)]==p[i]:
        c3+=1
notas=[c1,c2,c3]
z=max(c1,c2,c3)
r=[]
if z==notas[0]:
    r.append("Alvaro")
if z==notas[1]:
    r.append("Edwin")
if z==notas[2]:
    r.append("Gabriel")
print(z)
for d in range(len(r)):
    print(r[d])