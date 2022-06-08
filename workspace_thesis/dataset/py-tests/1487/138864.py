from sys import stdin
def esPrimo(n):
    if n<2:
        return False
    i=2
    while i*i <=n:
        if n%i==0:
            return False
        i=i+1
    return True

#n=int(input())
for n in stdin:
    n=int(n)
    if esPrimo(n):
        print("ES PRIMO")
    else:
        print("NO ES PRIMO")
