x=input()
i=1
aux=""
while i<len(x):
    if i%2==0 and x[i]=="u" or i%7==0:
        aux=aux+x[i]
    i=i+1
print(aux)
