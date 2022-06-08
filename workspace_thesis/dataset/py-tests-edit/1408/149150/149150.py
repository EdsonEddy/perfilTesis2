c1=0
c2=0
c3=0
alv=[ "A", "B", "C"]
edw=["B", "A", "B", "C"]
gab=["C", "C", "A", "A", "B", "B"]
qw=int(input())
pre=input()
for i in range(qw):
    if alv[i%len(alv)]==pre[i]:
        c1+=1
    if edw[i%len(edw)]==pre[i]:
        c2+=1
    if gab[i%len(gab)]==pre[i]:
        c3+=1
no=[c1,c2,c3]
v=max(c1,c2,c3)
cali=[]
if v==no[0]:
    cali.append("Alvaro")
if v==no[1]:
    cali.append("Edwin")
if v==no[2]:
    cali.append("Gabriel")
print(v)
for k in range(len(cali)):
    print(cali[k])