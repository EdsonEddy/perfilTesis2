alvaro=[ "A", "B", "C"]
edwin=["B", "A", "B", "C"]
gabriel=["C", "C", "A", "A", "B", "B"]
c1=0
c2=0
c3=0
z=int(input())
preg=input()
for i in range(z):
    if alvaro[i%len(alvaro)]==preg[i]:
        c1+=1
    if edwin[i%len(edwin)]==preg[i]:
        c2+=1
    if gabriel[i%len(gabriel)]==preg[i]:
        c3+=1
notas=[c1,c2,c3]
m=max(c1,c2,c3)
cali=[]
if m==notas[0]:
    cali.append("Alvaro")
if m==notas[1]:
    cali.append("Edwin")
if m==notas[2]:
    cali.append("Gabriel")
print(m)
for k in range(len(cali)):
    print(cali[k])