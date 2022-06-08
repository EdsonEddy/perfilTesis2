edwin=["B", "A", "B", "C"]
alvaro=[ "A", "B", "C"]
gabriel=["C", "C", "A", "A", "B", "B"]
he1=0
he2=0
he3=0
g=int(input())
preg=input()
for i in range(g):
    if alvaro[i%len(alvaro)]==preg[i]:
        he1+=1
    if edwin[i%len(edwin)]==preg[i]:
        he2+=1
    if gabriel[i%len(gabriel)]==preg[i]:
        he3+=1
nota=[he1,he2,he3]
a=max(he1,he2,he3)
cal=[]
if a==nota[0]:
    cal.append("Alvaro")
if a==nota[1]:
    cal.append("Edwin")
if a==nota[2]:
    cal.append("Gabriel")
print(a)
for c in range(len(cal)):
    print(cal[c])
