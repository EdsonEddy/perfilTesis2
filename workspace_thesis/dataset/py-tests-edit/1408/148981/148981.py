A,E,G=[ "A", "B", "C"],["B", "A", "B", "C"],["C", "C", "A", "A", "B", "B"]
a,b,c=0,0,0
n=int(input())
preguntas=input()
for i in range(n):
    if A[i%len(A)]==preguntas[i]:
        a+=1
    if E[i%len(E)]==preguntas[i]:
        b+=1
    if G[i%len(G)]==preguntas[i]:
        c+=1
total=[a,b,c]
l=max(a,b,c)
calificacion=[]
if l==total[0]:
    calificacion.append("Alvaro")
if l==total[1]:
    calificacion.append("Edwin")
if l==total[2]:
    calificacion.append("Gabriel")
print(l)
for j in range(len(calificacion)):
    print(calificacion[j])