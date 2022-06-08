alvaro=[ "A", "B", "C"]
edwin=["B", "A", "B", "C"]
gabriel=["C", "C", "A", "A", "B", "B"]
caso1=0
caso2=0
caso3=0
x=int(input())
preg=input()
for i in range(x):
    if alvaro[i%len(alvaro)]==preg[i]:
        caso1+=1
    if edwin[i%len(edwin)]==preg[i]:
        caso2+=1
    if gabriel[i%len(gabriel)]==preg[i]:
        caso3+=1
notas=[caso1,caso2,caso3]
m=max(caso1,caso2,caso3)
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
