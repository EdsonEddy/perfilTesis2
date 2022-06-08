import sys
def lectura4(n):
    sum=0
    cad=input()
    v=cad.split(" ")
    aux=[]
    for i in range(n):
            aux.append(v[i])
            sum=sum+int(aux[i])
    return (sum)
    
for n in sys.stdin:
    n=int(n)
    if n!=0:
        print(lectura4(n))
    else:
        break
