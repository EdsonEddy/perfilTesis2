alvaro=[ "A", "B", "C"]
edwin=["B", "A", "B", "C"]
gabriel=["C", "C", "A", "A", "B", "B"]
d1=0
d2=0
d3=0
a=int(input())
preg=input()
for i in range(a):
    if alvaro[i%len(alvaro)]==preg[i]:
        d1+=1
    if edwin[i%len(edwin)]==preg[i]:
        d2+=1
    if gabriel[i%len(gabriel)]==preg[i]:
        d3+=1
notas=[d1,d2,d3]
m=max(d1,d2,d3)
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