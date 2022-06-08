cad=input()
cad=cad.lower()
sw=False
for i in range(len(cad)-2):
    if(cad[i]=="o" and cad[i+1]=="r" and cad[i+2]=="o"):
        sw=True
        h=i
if(sw):
    print(h,h+2)
else:
    print(-1)