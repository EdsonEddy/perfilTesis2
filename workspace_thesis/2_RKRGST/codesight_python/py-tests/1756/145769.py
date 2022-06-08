casos=int(input())
for i in range(casos):
    limite=int(input())
    if limite>5:
        limite=limite%6
    s=2
    resp=(s**limite)*2
    while len(str(resp))>1:
        cadena=str(resp)
        lista=[]
        for z in cadena:
            lista.append(int(z))
        resp=sum(lista)
    print(resp)