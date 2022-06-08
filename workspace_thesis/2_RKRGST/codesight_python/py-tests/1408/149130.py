alvaro=[ "A", "B", "C"]
edwin=["B", "A", "B", "C"]
gabriel=["C", "C", "A", "A", "B", "B"]
C1=0
C2=0
C3=0
x=int(input())
preg=input()
for i in range(x):
    if alvaro[i%len(alvaro)]==preg[i]:
        C1+=1
    if edwin[i%len(edwin)]==preg[i]:
        C2+=1
    if gabriel[i%len(gabriel)]==preg[i]:
        C3+=1
notas=[C1,C2,C3]
m=max(C1,C2,C3)
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