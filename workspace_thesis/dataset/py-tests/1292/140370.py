import sys
def sumar(tam,cad):
    v=lee.split(" ")
    s=0
    for i in range(tam):
        s=s+int(v[i])
    return s  
for n in sys.stdin:
    n=int(n)
    #termina cuando n es 0 
    if n!=0:
        lee=input()
        print(sumar(n,lee))
    else:
        break