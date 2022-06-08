preguntas=int(input())
respuestas=list(input())
Alvaro=["A","B","C"]
Edwin=["B","A","B","C"]
Gabriel=["C","C","A","A","B","B"]
pA=pE=pG=0
rA=rE=rG=0
resp=[]
for i in range(preguntas):
    if respuestas[i]==Alvaro[pA]:
        rA+=1
    if respuestas[i]==Edwin[pE]:
        rE+=1
    if respuestas[i]==Gabriel[pG]:
        rG+=1
    pA+=1
    pE+=1
    pG+=1
    if pA==len(Alvaro):
        pA=0
    if pE==len(Edwin):
        pE=0
    if pG==len(Gabriel):
        pG=0
resp.append(rA)
resp.append(rE)
resp.append(rG)
mayor=max(resp)
final=[]
if mayor==rA:
    final.append("Alvaro")
if mayor==rE:
    final.append("Edwin")
if mayor==rG:
    final.append("Gabriel")
final.sort()
print(mayor)
for i in final:
    print(i)