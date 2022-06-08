c=str(input())
c=c+" "
lon=len(c)
sw=0
for i in range (0,lon):
    if c[i]=="o" or c[i]=="O":    
        if c[i+1]=="r" or c[i+1]=="R":
            if c[i+2]=="o" or c[i+2]=="O":
                sw=1    
                x=i                
if sw==1:
    print(x,x+2)
else:
    print(-1)       

