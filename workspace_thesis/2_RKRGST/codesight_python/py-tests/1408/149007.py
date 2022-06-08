alvaro=[ "A", "B", "C"]
edwin=["B", "A", "B", "C"]
gabriel=["C", "C", "A", "A", "B", "B"]
contador1=0
contador2=0
contador3=0
num=int(input())
pregunta=input()
for i in range(num):
    if alvaro[i%len(alvaro)]==pregunta[i]:
        contador1+=1
    if edwin[i%len(edwin)]==pregunta[i]:
        contador2+=1
    if gabriel[i%len(gabriel)]==pregunta[i]:
        contador3+=1
notas=[contador1,contador2,contador3]
m=max(contador1,contador2,contador3)
calificacion=[]
if m==notas[0]:
    calificacion.append("Alvaro")
if m==notas[1]:
    calificacion.append("Edwin")
if m==notas[2]:
    calificacion.append("Gabriel")
print(m)
for k in range(len(calificacion)):
    print(calificacion[k])
