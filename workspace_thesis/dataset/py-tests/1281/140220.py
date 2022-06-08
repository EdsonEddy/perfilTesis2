
def div(A, n):
    for i in range(1,int(n**0.5)+1 , 1):
        d = n % i
        if d == 0:
            A.append(i)
            if (n//i) != i:
             A.append(n//i)
import sys
for i in sys.stdin:
    n = int(i)
    A = []
    div(A,n)
    B=sorted(A)
    print("Divisores de",str(n)+":",*B)