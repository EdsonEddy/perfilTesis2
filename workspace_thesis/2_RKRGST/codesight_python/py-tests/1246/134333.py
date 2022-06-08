busc=input()
cad=input()
c=0
while cad.find(busc)!=-1:
    c+=1
    cad=cad[cad.find(busc)+1:]
print(c)