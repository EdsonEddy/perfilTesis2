def cambio(n):
    l = ["", "Ara", "da", "tra", "pra", "Hra", "Sea", "Xea", "gua", "noa", "Dea"]
    m=n//1000
    c=(n%1000)//100
    d=n%100
    res=""
    if m>0:
        m="Do "+str(l[m])
        res+=m
    if c>0:
        c=str(l[c])
        res=res+" "+c+"es"
    if d>0 and d<11:
        d=str(l[m])
        res+=d
    elif d>10 and d<=19:
        u=n%10
        d=" Dea "+str(l[u])
        res+=d
    elif d>19 and d<99:
        d1=d//10
        u=d%10
        d1=str(l[d1])
        u=str(l[u])
        print(d1,u)
        res+=d1+u
    return(res)

while True:
    n=int(input())
    print(cambio(n))
