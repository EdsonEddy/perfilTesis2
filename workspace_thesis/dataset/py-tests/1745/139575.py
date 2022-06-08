cp = 0
cn = 0
cd= 0
lista=[]
import sys
for i in sys.stdin:
    n=float(i)
    lista.append(i)
    cd=cd+1
    if(n>0):
        cp=cp+1
    elif n<0:
        cn=cn+1
    else:
        break
p=cd*100
pn=(cd-cp)*100
pt=((p-pn)//cn)-cd
print(pt)
print(max(lista))