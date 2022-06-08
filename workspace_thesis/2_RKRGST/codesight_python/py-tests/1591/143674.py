def GenerarPrimos(x):
    UltimoNmeroPrmo=2
    i=UltimoNmeroPrmo
    numeros=[True,True]+[True]*(x-1)
    while UltimoNmeroPrmo **2 <= x :
        i=i+UltimoNmeroPrmo
        while i <= x:
            numeros[i]=False
            i=i+UltimoNmeroPrmo
        j=UltimoNmeroPrmo+1
        while j < x:
            if numeros[j]:
                UltimoNmeroPrmo=j
                break
            j=j+1
        i=UltimoNmeroPrmo
    return [i+2 for i,z in enumerate (numeros[2:]) if z]

l=GenerarPrimos(1000000)
c=int(input())
for i in range (c):
    n=str(int(input()))
    p=''
    for d in n:
       if int(d) in l:
           p=p+d
    if p=='':
        print(-1)
    else:
        print(p)

