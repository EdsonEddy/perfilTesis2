def Ordenar(x,cd):
    nc=""
    i=0
    while(i<cd):
        if((x[i]!="Y" and x[i]!="y") and (x[i]!="A" and x[i]!="a") and (x[i]!="E" and x[i]!="e") and (x[i]!="I" and x[i]!="i") and (x[i]!="O" and x[i]!="o") and (x[i]!="U" and x[i]!="u")):
            nc=nc+"."
            nc=nc+x[i]
        i=i+1
    return(nc)

x=input()
cd=len(x)
R=Ordenar(x,cd)
print(R.lower())



