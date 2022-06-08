import sys
for n in sys.stdin:
    n=int(n)
    cad=input()
    c=0
    v = cad.split(" ")
    for i in range(n):
        v[i]=int(v[i])
    for j in range(1,n-1):
        if (v[j] > v[j-1] and v[j] > v[j+1]):
            c=c+1
        elif(v[j] < v[j-1] and v[j] < v[j+1]):
            c=c+1
    print(c)
    
