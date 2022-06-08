a,b,c=0,0,0
alv=[ "A", "B", "C"]
edw=["B", "A", "B", "C"]
gab=["C", "C", "A", "A", "B", "B"]

t=int(input())
cadena=input()
i=0
while i <(t):
    if gab[i%len(gab)]==cadena[i]:
        c+=1
    if alv[i%len(alv)]==cadena[i]:
        a+=1
    if edw[i%len(edw)]==cadena[i]:
        b+=1

    i+=1

notas=[a,b,c]
mm=max(a,b,c)
vec=[]
if mm==notas[0]:
    vec.append("Alvaro")
if mm==notas[1]:
    vec.append("Edwin")
if mm==notas[2]:
    vec.append("Gabriel")
print(mm)
j=0
while j < len(vec):
    print(vec[j])
    j+=1