c=str(input())
c1=""
lon=len(c)
for i in range (0,lon):
    if c[i]!="a" and c[i]!="A" and c[i]!="e" and c[i]!="E" and c[i]!="i" and c[i]!="I" and c[i]!="o" and c[i]!="O" and c[i]!="u" and c[i]!="U" and c[i]!="y" and c[i]!="Y":
        c1=c1+"."+c[i]
print(c1.lower())
