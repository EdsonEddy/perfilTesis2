c=int(input())
for i in range(c):
    a=int(input())
    l=input().split()
    l2=[]
    for j in l:
        l2.append(int(j))
    print(*sorted(l2))