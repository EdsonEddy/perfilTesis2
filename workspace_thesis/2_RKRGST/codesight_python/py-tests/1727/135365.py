a,b,c = map(int, input().split(" "))
cont=0
for j in range (a,b+1,1):
    if j%c==0:
        cont=cont+1 

print(cont)
