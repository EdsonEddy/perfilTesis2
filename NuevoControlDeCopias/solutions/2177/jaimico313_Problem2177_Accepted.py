def inter(variable):
    while variable>9:
        caso=str(variable);aux=0
        for i in caso:
           aux+=int(i)
        variable=aux
    return variable
for _ in range(int(input())):
    a,b=map(int,input().split())
    a1 =list(str(a));a2=len(a1);n=list()
    while a2>0 and len(a1)>=b:
        n.append(int("".join(list(reversed(a1[a2-b:])))))
        del a1[len(a1)-1]
        a2-=1
    palabra=list()
    for e in n:
        palabra.append(str(inter(e)))
    palabra.reverse()
    respuesta = ""
    if len(palabra)==0:
        respuesta+=""
    else:
        for e1 in palabra:
            respuesta+= e1
    print(respuesta)
