alvaro=[ "A", "B", "C"]
edwin=["B", "A", "B", "C"]
gabriel=["C", "C", "A", "A", "B", "B"]
a1=0
a2=0
a3=0
x=int(input())
preg=input()
for i in range(x):
    if alvaro[i%len(alvaro)]==preg[i]:
        a1+=1
    if edwin[i%len(edwin)]==preg[i]:
        a2+=1
    if gabriel[i%len(gabriel)]==preg[i]:
        a3+=1
notas=[a1,a2,a3]
m=max(a1,a2,a3)
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