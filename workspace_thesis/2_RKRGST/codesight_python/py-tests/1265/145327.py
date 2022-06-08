def convertir_monedas(peniques):
 
    libra = peniques //20 //12
    chelin= peniques //12 %20
    peniques= peniques %12
    return libra, chelin ,peniques
 
cantidad_monedas=int(input())
if cantidad_monedas>=0 and cantidad_monedas<=10000:
 
    l,c,p=convertir_monedas(cantidad_monedas)
 
    print ("(", end="")
    print (l, end="")
    print (",", c,end="")
    print (",", end=" ")
    print (p,end="")
    print (")",end="")