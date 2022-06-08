cad=str(input())
n=len(cad)+1

c=0
for i in range(0,len(cad)):
    if cad[i]=="c":
        c=c+1
print(c)