alvaro=[ "A", "B", "C"]
edwin=["B", "A", "B", "C"]
gabriel=["C", "C", "A", "A", "B", "B"]
j1=0
j2=0
j3=0
x=int(input())
preg=input()
for i in range(x):
    if alvaro[i%len(alvaro)]==preg[i]:
        j1+=1
    if edwin[i%len(edwin)]==preg[i]:
        j2+=1
    if gabriel[i%len(gabriel)]==preg[i]:
        j3+=1
notas=[j1,j2,j3]
m=max(j1,j2,j3)
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