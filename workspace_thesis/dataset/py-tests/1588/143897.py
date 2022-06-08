def num():
    numDeDatos=int(input())
    y=[]
    numn=map(int,input().split())
    y.extend(numn)
    zi=y[:numDeDatos]
    return zi


numDeentradas=int(input())
while numDeentradas>0:
    lg=num()
    #lg=[3, 1, 4, 1, 5, 9, 2, 6, 5]
    lp=[]
    gp=[]
    sol=[]
    lg.sort()#ordena la lista
    """for i in lg:
        if i not in lp:
            lp.append(i)#añade si no esta en la segunda lista"""
    for i in lg:
        abc= (i *2)%3
        if abc==0:
            gp.append(i)
    for j in gp:
        bg=j*2
        sol.append(bg)
    print("La suma es "+str(sum(sol)))
    numDeentradas-=1