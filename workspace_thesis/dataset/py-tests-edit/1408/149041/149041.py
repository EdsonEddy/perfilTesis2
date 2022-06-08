alvaro=[ "A", "B", "C"]
edwin=["B", "A", "B", "C"]
gabriel=["C", "C", "A", "A", "B", "B"]
m1=0
m2=0
m3=0
y=int(input())
prg=input()
for i in range(y):
    if alvaro[i%len(alvaro)]==prg[i]:
        m1+=1
    if edwin[i%len(edwin)]==prg[i]:
        m2+=1
    if gabriel[i%len(gabriel)]==prg[i]:
        m3+=1
notas=[m1,m2,m3]
p=max(m1,m2,m3)
cali=[]
if p==notas[0]:
    cali.append("Alvaro")
if p==notas[1]:
    cali.append("Edwin")
if p==notas[2]:
    cali.append("Gabriel")
print(p)
for k in range(len(cali)):
    print(cali[k])