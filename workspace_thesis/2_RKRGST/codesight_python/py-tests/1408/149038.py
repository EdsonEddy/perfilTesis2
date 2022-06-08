alvaro=[ "A", "B", "C"]
edwin=["B", "A", "B", "C"]
gabriel=["C", "C", "A", "A", "B", "B"]
d1=0
d2=0
d3=0
y=int(input())
preg=input()
for i in range(y):
    if alvaro[i%len(alvaro)]==preg[i]:
        d1+=1
    if edwin[i%len(edwin)]==preg[i]:
        d2+=1
    if gabriel[i%len(gabriel)]==preg[i]:
        d3+=1
notas=[d1,d2,d3]
z=max(d1,d2,d3)
cali=[]
if z==notas[0]:
    cali.append("Alvaro")
if z==notas[1]:
    cali.append("Edwin")
if z==notas[2]:
    cali.append("Gabriel")
print(z)
for f in range(len(cali)):
    print(cali[f])