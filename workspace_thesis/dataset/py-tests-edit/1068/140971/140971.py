n=int(input())
for j in range(n):
    s=0
    g=int(input())
    for i in range(g):

        l=str(input())
        if l!="porque":
            s=s+1
        else:
            print(s)