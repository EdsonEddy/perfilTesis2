Alvaro=[ "A", "B", "C"]
Edwin=["B", "A", "B", "C"]
Gabriel=["C", "C", "A", "A", "B", "B"]
C1=0
C2=0
C3=0
x=int(input())
preg=input()
for i in range(x):
    if Alvaro[i%len(Alvaro)]==preg[i]:
        C1+=1
    if Edwin[i%len(Edwin)]==preg[i]:
        C2+=1
    if Gabriel[i%len(Gabriel)]==preg[i]:
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