while True:
    variables=input().split()
    base=int(variables[1])
    cont=len(variables[0])-1
    newnum=0
    for i in variables[0]:
        newnum=int(i)*(base**cont)+newnum
        cont-=1
    print(newnum)