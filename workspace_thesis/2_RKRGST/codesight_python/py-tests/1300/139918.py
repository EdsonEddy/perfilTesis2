import sys
def contar(tam,cad):
    v=s.split(" ")
    cd=0
    for i in range(len(v)):
      if(v[i]==v[tam-1]):
         cd+=1
    return cd  

for n in sys.stdin:
    n=int(n)
    s=input()
    print(contar(n,s))
        

