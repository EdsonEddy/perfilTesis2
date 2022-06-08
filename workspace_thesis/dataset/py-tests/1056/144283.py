m=int(input())
for i in range(m):
    n=int(input())
    txt=input()
    v=txt.split()
    v.reverse()
    for i in range(len(v)):
        print(v[i],end=" ")
    print()