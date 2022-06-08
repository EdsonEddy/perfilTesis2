n=int(input())
for i in range(n):
    cad=input()
    v=list(map(int,cad.split()))
    c=0
    for i in range(1,len(v)):
        if v[i]>v[i-1]:
            c=c+1
    print(c)
        
        