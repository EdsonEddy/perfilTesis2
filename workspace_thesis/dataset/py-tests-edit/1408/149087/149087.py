a=[ "A", "B", "C"]
e=["B", "A", "B", "C"]
g=["C", "C", "A", "A", "B", "B"]
contador1=0
contador2=0
contador3=0
x=int(input())
y=input()
for i in range(x):
    #print(a[i%len(a)])
    if a[i%len(a)]==y[i]:
        contador1+=1
    if e[i%len(e)]==y[i]:
        contador2+=1
    if g[i%len(g)]==y[i]:
        contador3+=1
nota=[contador1,contador2,contador3]
#print(nota)
m=max(contador1,contador2,contador3)
me=[]
if m==nota[0]:
    me.append("Alvaro")
if m==nota[1]:
    me.append("Edwin")
if m==nota[2]:
    me.append("Gabriel")
print(m)
for o in range(len(me)):
    print(me[o])
