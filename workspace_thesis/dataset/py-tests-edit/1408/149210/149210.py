alvaro=[ "A", "B", "C"]
edwin=["B", "A", "B", "C"]
gabriel=["C", "C", "A", "A", "B", "B"]
p1=0
p2=0
p3=0
x=int(input())
preg=input()
for i in range(x):
    if alvaro[i%len(alvaro)]==preg[i]:
        p1+=1
    if edwin[i%len(edwin)]==preg[i]:
        p2+=1
    if gabriel[i%len(gabriel)]==preg[i]:
        p3+=1
notas=[p1,p2,p3]
m=max(p1,p2,p3)
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
#140888888888 