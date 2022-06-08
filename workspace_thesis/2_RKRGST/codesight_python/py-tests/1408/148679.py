n=int(input())
resc=input()
l=[]
for j in resc:
    l.append(j)
la=["A","B","C"]*n
le=["B","A","B","C"]*n
lg=["C","C","A","A","B","B"]*n
ca,ce,cg=0,0,0
for i in range(n):
    if l[i]==la[i]:
        ca=ca+1
    if l[i]==le[i]:
        ce=ce+1
    if l[i]==lg[i]:
        cg=cg+1
if ca>ce and ca>cg or ca==ce or ca==cg:
    print(ca)
    print("Alvaro")
    if ca==ce:
        print("Gabriel")
    if ca==cg:
        print("Edwin")
elif ce>cg or ce==cg or ce==ca:
    print(ce)
    print("Edwin")
    if ce==cg:
        print("Gabriel")
else:
    print(cg)
    print("Gabriel")