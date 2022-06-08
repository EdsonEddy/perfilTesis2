t=int(input())
while t>0:
    dic={}
    alf=input()
    cad=input()
    for i in range(len(alf)):
        dic[alf[i]]=i
    pi=dic[cad[0]]
    resu=0
    for i in range(1,len(cad)):
        ps=0
        rr=dic[cad[i]]
        if rr<pi:
            for j in range(rr, pi):
                ps+=1
        else:
            for j in range(pi, rr):
                ps+=1
        pi=rr
        resu+=ps
         
    print(resu)
    t-=1