alvaro=[ "A", "B", "C"]
edwin=["B", "A", "B", "C"]
gabriel=["C", "C", "A", "A", "B", "B"]
d1=0
d2=0
d3=0
p=int(input())
preg=input()
for i in range(p):
    if alvaro[i%len(alvaro)]==preg[i]:
        d1+=1
    if edwin[i%len(edwin)]==preg[i]:
        d2+=1
    if gabriel[i%len(gabriel)]==preg[i]:
        d3+=1
notas=[d1,d2,d3]
o=max(d1,d2,d3)
cali=[]
if o==notas[0]:
    cali.append("Alvaro")
if o==notas[1]:
    cali.append("Edwin")
if o==notas[2]:
    cali.append("Gabriel")
print(o)
for k in range(len(cali)):
    print(cali[k])