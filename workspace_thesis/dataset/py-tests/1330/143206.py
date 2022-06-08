cad,pos=map(str,input().split())
i=len(cad)-int(pos)
aux1=cad[:i]
aux2=cad[i:]
print("{}{}".format(aux2,aux1))