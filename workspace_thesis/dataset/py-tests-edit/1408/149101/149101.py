exam=[]
pq,pw,pe=0,0,0
alvaro=[ "A", "B", "C"]
edwin=["B", "A", "B", "C"]
gabriel=["C", "C", "A", "A", "B", "B"]

x=int(input())
preg=input()
for i in range(x):
    if alvaro[i%len(alvaro)]==preg[i]:
        pq+=1
    if edwin[i%len(edwin)]==preg[i]:
        pw+=1
    if gabriel[i%len(gabriel)]==preg[i]:
        pe+=1
notas=[pq,pw,pe]
m=max(pq,pw,pe)
if m==notas[0]:
    exam.append("Alvaro")
if m==notas[1]:
    exam.append("Edwin")
if m==notas[2]:
    exam.append("Gabriel")
print(m)
for k in range(len(exam)):
    print(exam[k])