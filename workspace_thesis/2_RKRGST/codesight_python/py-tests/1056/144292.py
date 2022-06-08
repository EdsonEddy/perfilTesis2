r=int(input())
for i in range(r):
    n=int(input())
    cad=input()
    v=list(map(int,cad.split()))
    v.reverse()
    for i in range(len(v)):
        print(v[i],end=" ")
    print()