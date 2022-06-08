cad=input().lower()
c=input().lower()
n= len(cad)
i=0
while(i < len(cad)):
    m=cad[i:]
    if c in m:
        print (m.index(c)+i)
        i +=m.index(c)
    i+=1
    
        

